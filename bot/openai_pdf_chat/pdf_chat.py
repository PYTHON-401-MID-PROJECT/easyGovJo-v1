from dotenv import load_dotenv 
from langchain.text_splitter import RecursiveCharacterTextSplitter   
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS  
import pickle  
import os 
from langchain.chat_models import ChatOpenAI  
from langchain.chains.question_answering import load_qa_chain 

def main(incoming_msg):
    
    load_dotenv() 

    text_splitter = RecursiveCharacterTextSplitter(  
            chunk_size=10000, 
            chunk_overlap=200,
            length_function=len
            )                   

    folder_path = '../data_/' 

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  
        if os.path.isfile(file_path) and file_path.endswith(".txt") :  
            with open(file_path, 'r',encoding='utf-8') as file:
                string_data = file.read()
                chunks = text_splitter.split_text(text=string_data)     
                store_name = file.name[:-4]  

                if os.path.exists(f"{store_name}.pkl"):       
                    with open(f"{store_name}.pkl", "rb") as f:
                        VectorStore = pickle.load(f)
                else:
                    embeddings = OpenAIEmbeddings()
                    VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
                    with open(f"{store_name}.pkl", "wb") as f:
                        pickle.dump(VectorStore, f)
    
    if incoming_msg:
        docs = VectorStore.similarity_search(query=incoming_msg, k=2)
        llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        chain = load_qa_chain(llm=llm, chain_type="stuff") 
        response = chain.run(question=incoming_msg,input_documents=docs)
        return response
