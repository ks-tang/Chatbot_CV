from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def build_vectorstore():
    # Charger le texte
    loader = TextLoader("data/documents/cv.txt", encoding="utf-8")
    docs = loader.load()

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Embedding
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Index
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local("data/faiss_index")

if __name__ == "__main__":
    build_vectorstore()
