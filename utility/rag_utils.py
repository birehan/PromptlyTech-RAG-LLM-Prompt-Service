import json

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate


from logger import logger
from datasets import Dataset
import random

import weaviate
from dotenv import load_dotenv,find_dotenv
from weaviate.embedded import EmbeddedOptions

from ragas import evaluate
from ragas.metrics import ( faithfulness, answer_relevancy, context_recall, context_precision)

 
# Load OpenAI API key from .env file
load_dotenv(find_dotenv())


def data_loader(file_path= '../prompts/context.txt', chunk_size=500, chunk_overlap=50):
    try:
        loader = TextLoader(file_path)
        documents = loader.load()

        # Chunk the data
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.split_documents(documents)
        
        logger.info("data loaded to vector database successfully")
        return chunks
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 


def create_langchain_pipeline(retriever, template, temperature=0):
    try:
        # Define LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)

        # Define prompt template
        
        prompt = ChatPromptTemplate.from_template(template)

        # Setup RAG pipeline
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()} 
            | prompt 
            | llm
            | StrOutputParser() 
        )

        logger.info("langchain with rag pipeline created successfully.")
        return rag_chain

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
    

def generate_testcase_and_context(questions, ground_truths, retriever, rag_chain):
    try:
        answers = []
        contexts = []

        # Inference
        for query in questions:

            answers.append(rag_chain.invoke(query))
            contexts.append([docs.page_content for docs in retriever.get_relevant_documents(query)])

            
        data = {
            "question": questions, # list 
            "answer": answers, # list
            "contexts": contexts, # list list
            "ground_truths": ground_truths # list Lists
        }


        # Convert dict to dataset
        dataset = Dataset.from_dict(data) 
        logger.info("automatic evaluation data generated succesfully.")

        return  dataset
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
    

def create_retriever(chunks):
    try:
        
        # Load OpenAI API key from .env file
        load_dotenv(find_dotenv())


        # Setup vector database
        client = weaviate.Client(
            embedded_options = EmbeddedOptions()
        )

        # Populate vector database
        vectorstore = Weaviate.from_documents(
            client = client,    
            documents = chunks,
            embedding = OpenAIEmbeddings(),
            by_text = False
        )

        # Define vectorstore as retriever to enable semantic search
        retriever = vectorstore.as_retriever()
        logger.info("automatic evaluation data generated succesfully.")

        return retriever
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
    
def monte_carlo_eval(prompt):
    try:
        # Simulating different types of responses
        response_types = ['highly relevant', 'somewhat relevant', 'irrelevant']
        scores = {'highly relevant': 3, 'somewhat relevant': 2, 'irrelevant': 1}

        # Perform multiple random trials
        trials = 100
        total_score = 0
        for _ in range(trials):
            response = random.choice(response_types)
            total_score += scores[response]

        # Average score represents the evaluation
        return total_score / trials
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def elo_eval(prompt, base_rating=1500):
    try:

        # Simulate the outcome of the prompt against standard criteria
        # Here, we randomly decide if the prompt 'wins', 'loses', or 'draws'
        outcomes = ['win', 'loss', 'draw']
        outcome = random.choice(outcomes)

        # Elo rating formula parameters
        K = 30  # Maximum change in rating
        R_base = 10 ** (base_rating / 400)
        R_opponent = 10 ** (1600 / 400)  # Assuming a fixed opponent rating
        expected_score = R_base / (R_base + R_opponent)

        # Calculate the new rating based on the outcome
        actual_score = {'win': 1, 'loss': 0, 'draw': 0.5}[outcome]
        new_rating = base_rating + K * (actual_score - expected_score)
    
        return new_rating
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def elo_ratings_func(prompts, elo_ratings, K=30, opponent_rating=1600):
    """
    Update Elo ratings for a list of prompts based on simulated outcomes.

    Parameters:
    prompts (list): List of prompts to be evaluated.
    elo_ratings (dict): Current Elo ratings for each prompt.
    K (int): Maximum change in rating.
    opponent_rating (int): Fixed rating of the opponent for simulation.

    Returns:
    dict: Updated Elo ratings.
    """
    try:

        for prompt in prompts:
            # Simulate an outcome against the standard criteria or another prompt
            outcome = random.choice(['win', 'loss', 'draw'])

            # Calculate the new rating based on the outcome
            actual_score = {'win': 1, 'loss': 0, 'draw': 0.5}[outcome]
            R_base = 10 ** (elo_ratings[prompt] / 400)
            R_opponent = 10 ** (opponent_rating / 400)
            expected_score = R_base / (R_base + R_opponent)
            elo_ratings[prompt] += K * (actual_score - expected_score)

        return elo_ratings

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def evaluate_prompt(main_prompt, test_cases):
    try:
        evaluations = {}

        # Evaluate the main prompt using Monte Carlo and Elo methods
        evaluations['main_prompt'] = {
            'Monte Carlo Evaluation': monte_carlo_eval(main_prompt),
            'Elo Rating Evaluation': elo_eval(main_prompt)
        }

        # Evaluate each test case
        for idx, test_case in enumerate(test_cases):
            evaluations[f'test_case_{idx+1}'] = {
                'Monte Carlo Evaluation': monte_carlo_eval(test_case),
                'Elo Rating Evaluation': elo_eval(test_case)
            }

        return evaluations

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def load_file(file_path):
    try:

        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()   
        
        return file_contents
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 

def ragas_evaulation(response):
    try:
        result = evaluate(
            dataset = response, 
            metrics=[
                context_precision,
                context_recall,
                faithfulness,
                answer_relevancy,
            ],
        )

        df = result.to_pandas()
        return df

      
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 



def get_generated_prompt_with_evaulation(question):
    try:
        chunks = data_loader()
        retriever = create_retriever(chunks)

        prompt_template = load_file('../prompts/prompt-generation-prompt.txt')
        evaluation_tempate = load_file('../prompts/evaluation-data-generation.txt')


        prompt_rag_chain = create_langchain_pipeline(retriever, prompt_template)
        evaulation_rag_chain = create_langchain_pipeline(retriever, evaluation_tempate, temperature=0.2)


        generated_prompts = prompt_rag_chain.invoke(question)
        prompt_list  = json.loads(generated_prompts)
        # Extract prompt values and ground truth values into separate lists

        questions = [item['prompt'] for item in prompt_list]
        ground_truths = [[item['ground_truth']] for item in prompt_list]


        response = generate_testcase_and_context(questions, ground_truths, retriever, evaulation_rag_chain)
        df = ragas_evaulation(response)

        return df
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
