from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def load_rag_chain():
    # Charger l'index vectoriel
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("data/faiss_index", embedding)

    # Charger modèle Mistral via Ollama
    llm = Ollama(model="mistral")

    # Création de la chaîne RAG
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return chain

# Interface simple
def ask(query):
    chain = load_rag_chain()
    result = chain.run(query)
    return result
