from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .embeddings import CohereEmbedding
from langchain_community.vectorstores import Chroma

def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def load_url(url: str):
    loader = WebBaseLoader(url)
    return loader.load()

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len
    )
    return splitter.split_documents(documents)

def create_vector_store(chunks):
    embeddings = CohereEmbedding()
    return Chroma.from_documents(chunks, embedding=embeddings)

def get_context_form_document(file_path: str=None, url: str=None):
    try:
        if file_path:
            docs = load_pdf(file_path)
        elif url:
            docs = load_url(url) 
        chunks = split_documents(docs)
        vector_store = create_vector_store(chunks)  
        retriever_from_pdf = vector_store.as_retriever(search_kwargs={"k": 7})
        return retriever_from_pdf
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None