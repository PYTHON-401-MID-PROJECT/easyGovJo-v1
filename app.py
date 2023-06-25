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

def main():
    
    load_dotenv()  #to load open Ai API key
    st.header("Gov Chat Bot") # to write header in the web



    text_splitter = RecursiveCharacterTextSplitter(  
            chunk_size=10000, 
            chunk_overlap=200,
            length_function=len
            )                   # to split the text file into chunks (parts)

    folder_path = './txt_data/'  # Replace with the actual path to your folder

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  # Create the full file path
        if os.path.isfile(file_path) and file_path.endswith(".txt") :  # Check if it's a file (not a folder)
            with open(file_path, 'r',encoding='utf-8') as file:
                string_data = file.read()
                chunks = text_splitter.split_text(text=string_data)     # to split the text file into chunks (parts)
                store_name = file.name[:-4]  # to save the pdf file name without the extention

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
        # st.write("--------------------")
        # st.write(docs[0].page_content)
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
