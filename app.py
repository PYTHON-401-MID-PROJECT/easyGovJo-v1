import streamlit as st    #web service provider 
from dotenv import load_dotenv #to load open Ai API key
from langchain.embeddings.openai import OpenAIEmbeddings # to convert text to embeddings
from langchain.vectorstores import FAISS  # to convert text to embeddings
import pickle  # to save embeddings
import os #  to deal with file path
from langchain.chat_models import ChatOpenAI  # to deal with chat GPT
from langchain.chains.question_answering import load_qa_chain  # to deal with chat GPT
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff
 






def main():
    
    load_dotenv()  #to load open Ai API key
    st.header("Gov Chat Bot") # to write header in the web
    
    loader = DirectoryLoader('txt_data', glob="**/*.txt")
    documents = loader.load()
    st.write(documents)
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)


    if os.path.exists("data.pkl"):      # True --> we worked this file befor 
        with open("data.pkl", "rb") as f:
            db = pickle.load(f)
        st.write('Embeddings Loaded from the Disk')

    else:
        embeddings = OpenAIEmbeddings()
     
        @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
        def completion_with_backoff(**kwargs):
            return openai.Completion.create(**kwargs)
        
        completion_with_backoff(db = FAISS.from_documents(docs, embeddings))

        with open("data.pkl", "wb") as f:
            pickle.dump(db, f)
        st.write('Embeddings computaion')




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
