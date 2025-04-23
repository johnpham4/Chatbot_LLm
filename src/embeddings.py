from openai import OpenAI
from langchain.embeddings.base import Embeddings
import os
import dotenv
from typing import List
dotenv.load_dotenv()

class CohereEmbedding(Embeddings):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(
            api_key=os.getenv("COHERE_API_KEY"),
            base_url="https://api.cohere.ai/compatibility/v1"
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        response = self.client.embeddings.create(
            input=texts,
            model="embed-v4.0",
            encoding_format="float"
        )
        return [d.embedding for d in response.data]

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]