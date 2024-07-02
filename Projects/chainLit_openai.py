import os
from openai import AsyncOpenAI
import chainlit as cl

from keys import api_key

print(cl)


client = AsyncOpenAI(api_key=api_key)

settings = {
    "model": "gpt-4o",
    "temperature": 0
}

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )

@cl.on_message
async def main(message: cl.Message):
    # Read the context from the file
    with open('code.py', 'r') as file:
        context = file.read()

    # Define the prompt with the dynamic question
    question = message.content
    prompt = f"{context}\n\nQuestion: {question}"

    message_history = [{"role": "system", "content": "You are a helpful assistant."}]
    message_history.append({"role": "user", "content": prompt})

    msg = cl.Message(content="")
    await msg.send()

    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
