import streamlit as st    #web service provider 
from dotenv import load_dotenv #to load open Ai API key
from PyPDF2 import PdfReader  # read pdf files
from langchain.text_splitter import RecursiveCharacterTextSplitter   # to manipulate text 
from langchain.embeddings.openai import OpenAIEmbeddings # to convert text to embeddings
from langchain.vectorstores import FAISS  # to convert text to embeddings
import pickle  # to save embeddings
import os #  to deal with file path
from langchain.chat_models import ChatOpenAI  # to deal with chat GPT
from langchain.chains.question_answering import load_qa_chain  # to deal with chat GPT
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

def main():
    
    load_dotenv()  #to load open Ai API key
    st.header("Gov Chat Bot") # to write header in the web

    loader = DirectoryLoader('txt_data', glob="**/*.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)


    query = st.text_input("Ask questions about your data:")
 
    if query:
        docs = db.similarity_search(query=query, k=1)
        # st.write("--------------------")
        st.write(docs)
        # st.write("--------------------")
        # st.write(docs[1].page_content)
        # st.write("--------------------")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        st.write(llm)
        # st.write(chain.llm_chain.prompt.template) 
        st.write("-----------------------------------------")
        response = chain.run(question=query,input_documents=docs)
        st.write(response)

if __name__ == "__main__":
    main()
