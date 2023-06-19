import streamlit as st    #web service provider 
from dotenv import load_dotenv #to load open Ai API key
from PyPDF2 import PdfReader  # read pdf files
from langchain.text_splitter import RecursiveCharacterTextSplitter   # to manipulate text 
from langchain.embeddings.openai import OpenAIEmbeddings # to convert text to embeddings
from langchain.vectorstores import FAISS  # to convert text to embeddings
import pickle  # to save embeddings
import os #  to deal with file path
from langchain.llms import OpenAI  # to deal with chat GPT
from langchain.chains.question_answering import load_qa_chain  # to deal with chat GPT


def main():

    load_dotenv()  #to load open Ai API key
    st.header("Gov Chat Bot") # to write header in the web
    pdf = st.file_uploader("update the bot data" , type="pdf")  # to write pdf uploader feald in the web

    if pdf is not None:
        pdf_reader = PdfReader(pdf) #read the pdf
        # st.write(pdf_reader)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()  # convert the pdf text 
        # st.write(text)

        text_splitter = RecursiveCharacterTextSplitter(  
            chunk_size=1000, 
            chunk_overlap=200,
            length_function=len
            )                   # to split the text file into chunks (parts)

        chunks = text_splitter.split_text(text=text)     # to split the text file into chunks (parts)

        store_name = pdf.name[:-4]  # to save the pdf file name without the extention

        if os.path.exists(f"{store_name}.pkl"):      # True --> we worked this file befor 
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
            st.write('Embeddings Loaded from the Disk')

        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            st.write('Embeddings computaion')


    query = st.text_input("Ask questions about your data:")
 
    if query:
        docs = VectorStore.similarity_search(query=query, k=2)
        # st.write(docs)
        llm = OpenAI()
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        response = chain.run(question=query,input_documents=docs)
        st.write(response)

if __name__ == "__main__":
    main()
