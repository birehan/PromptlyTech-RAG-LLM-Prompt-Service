import requests
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter  
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv,find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions
from dotenv import load_dotenv,find_dotenv
# 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from logger import logger

from datasets import Dataset


# Data loader
def data_loader(file_path= '../prompts/context.txt', chunk_size=500, chunk_overlap=50):
    try:
        loader = TextLoader(file_path)
        documents = loader.load()

        # Chunk the data
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.split_documents(documents)
        
        logger.info("data loaded to vector database successfullu")
        return chunks
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 


def create_chain_rag(retriever, template):
    try:
        # Define LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        # Define prompt template
        
       
        prompt = ChatPromptTemplate.from_template(template)

        # Setup RAG pipeline
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()} 
            | prompt 
            | llm
            | StrOutputParser() 
        )

        logger.info("data loaded to vector database successfully")
        return rag_chain

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None 
    

def generate_testcase_and_context(questions, ground_truths, retriever, template):
    try:
        answers = []
        contexts = []

        rag_chain = create_chain_rag(retriever, template)

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
    