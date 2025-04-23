import os
from typing import List, Tuple, Generator
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from pdf_utils import load_pdf, split_documents, create_vector_store
import warnings

warnings.filterwarnings("ignore")
load_dotenv(find_dotenv())

retriever_from_pdf = None  

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.getenv('FIREWORKS_API_KEY')
)

def chat_completion(messages: List[dict]) -> Generator[str, None, None]:
    try:
        response = client.chat.completions.create(
            model='accounts/fireworks/models/llama-v3p1-405b-instruct',
            messages=messages,
            stream=True,
            temperature=0.7,
            max_tokens=1000,
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        print(f"Error in chat_completion: {str(e)}")

def get_context_from_pdf(file_path: str):
    """Tạo retriever từ file PDF và lưu vào biến toàn cục."""
    global retriever_from_pdf
    try:
        docs = load_pdf(file_path)    
        chunks = split_documents(docs)
        vector_store = create_vector_store(chunks)  
        retriever_from_pdf = vector_store.as_retriever(search_kwargs={"k": 7})
    except Exception as e:
        print(f"Error loading PDF: {e}")
        retriever_from_pdf = None

def format_chat_history(chat_history: List[Tuple[str, str]]) -> List[dict]:
    messages = [{
        'role': 'system',
        'content': (
            "You are a knowledgeable and helpful assistant. "
            "When responding to queries that include context from documents, "
            "combine that information with your own knowledge to give clear and complete answers."
        )
    }]

    if retriever_from_pdf and chat_history and chat_history[-1][0]:
        query = chat_history[-1][0]
        try:
            relevant_docs = retriever_from_pdf.get_relevant_documents(query)
            context = "\n\n".join([doc.page_content for doc in relevant_docs])
            if context:
                messages.append({
                    'role': 'system',
                    'content': f"Here is some context from the uploaded document:\n\n{context}"
                })
        except Exception as e:
            print(f"Error retrieving context: {e}")

    for user_msg, bot_msg in chat_history:
        if user_msg:
            messages.append({'role': 'user', 'content': user_msg})
        if bot_msg:
            messages.append({'role': 'assistant', 'content': bot_msg})

    return messages

def generate_response(chat_history: List[Tuple[str, str]]) -> Generator[List[Tuple[str, str]], None, None]:
    if not chat_history or not chat_history[-1][0]:
        yield chat_history
        return

    chat_history[-1] = (chat_history[-1][0], "")  
    messages = format_chat_history(chat_history)

    full_response = ""
    for token in chat_completion(messages):
        full_response += token
        chat_history[-1] = (chat_history[-1][0], full_response)
        yield chat_history

def set_user_response(user_message: str, chat_history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
    if not user_message.strip():
        return user_message, chat_history

    chat_history = chat_history or []
    chat_history.append((user_message, None))
    return "", chat_history


