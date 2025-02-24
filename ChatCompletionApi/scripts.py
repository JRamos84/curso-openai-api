import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "Te llamas Vision, presentate como tal",       
        },
        {
            "role": "user",
            "content": "Hola, como estas"
        },
        {
            "role": "assistant",
            "content":"Hola! Soy Visión, un asistente virtual listo para ayudarte. ¿En qué puedo asisterte hoy?"
        },
        {
            "role":"user",
            "content":"Qué es Visión"
        }
    ],
    max_tokens=100,
    temperature=0.7
)

print(response.choices[0].message.content)