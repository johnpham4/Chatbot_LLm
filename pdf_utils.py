from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from embeddings import CohereEmbedding
from langchain_community.vectorstores import Chroma

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

def create_vector_store(chunks):
    embeddings = CohereEmbedding()
    return Chroma.from_documents(chunks, embedding=embeddings)
