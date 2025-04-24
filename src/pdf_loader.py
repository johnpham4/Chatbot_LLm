from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .embeddings import CohereEmbedding
from langchain_community.vectorstores import Chroma
import os

def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len
    )
    return splitter.split_documents(documents)


VECTOR_DIR = "./vector_store"

def create_vector_store(chunks):
    embeddings = CohereEmbedding()
    os.makedirs(VECTOR_DIR, exist_ok=True)
    return Chroma.from_documents(
        chunks, embedding=embeddings, persist_directory=VECTOR_DIR
    )


def initial_vector_store(chunks=None):
    embeddings = CohereEmbedding()
    if os.path.exists(VECTOR_DIR) and os.listdir(VECTOR_DIR):
        return Chroma(persist_directory=VECTOR_DIR, embedding_function=embeddings)
    elif chunks:
        return create_vector_store(chunks)
    else:
        return None
    
def get_context_from_pdf(file_path: str):
    try:
        docs = load_pdf(file_path)    
        chunks = split_documents(docs)

        vector_store = initial_vector_store()

        if vector_store is None:
            vector_store = create_vector_store(chunks)
        else:
            vector_store.add_documents(chunks)
            vector_store.persist() 
        return vector_store.as_retriever(search_kwargs={"k": 7})
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

    