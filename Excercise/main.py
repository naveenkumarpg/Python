from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from keys import api_key

embeddings = OpenAIEmbeddings(openai_api_key=api_key)

emb = embeddings.aembed_query('Hello there, How are you ?')

print(emb)
