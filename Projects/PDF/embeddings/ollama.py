from langchain_community.embeddings import OllamaEmbeddings

embeddings = (OllamaEmbeddings())  

def create_embedding_ollama(content):
  return embeddings.embed_query(content)
  
  
