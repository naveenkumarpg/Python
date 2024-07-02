from langchain_openai import ChatOpenAI
from server.embeddings.keys import api_key

llm = ChatOpenAI(
    openai_api_key=api_key,
    model="gpt-4o"
)

def generate_comments_open_ai(data):
  messages = [
      ("system","I mam new to the COBOL programming, you being expert in understanding the code better, please help me by explaining what this code does and add details comments to the every functionality on this code",),
      ("human", f'{data}'),
  ]
  ai_msg = llm.invoke(messages)
  return ai_msg.content
