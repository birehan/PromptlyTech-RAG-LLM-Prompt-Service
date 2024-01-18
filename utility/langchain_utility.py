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


def create_chain_rag(retriever):
    try:
        # Define LLM
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

        # Define prompt template
        template = """
        You are a prompt generator which generate a list of prompts for the user
        question.  Use the following pieces of retrieved context to answer the question. 
        If you don't know the answer, just say that you don't know. 
        Use two sentences maximum and keep the answer concise. return a list of 5 prompts. 
        do not give the generated questions number like 1. 2.
        separate the questions based on new line.
        Question: {question} 
        Context: {context} 
        Answer:
        """

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