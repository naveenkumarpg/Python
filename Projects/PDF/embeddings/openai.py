from langchain_openai import OpenAIEmbeddings
from embeddings.keys import api_key

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",openai_api_key=api_key)

def create_embedding_open_ai(content):
  return embeddings.embed_query(content)
