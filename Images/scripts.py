import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64decode(image_file.read()).decode("utf-8")

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "Eres un asistente que analiza las imagenes con gran detalles"
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Hola, ¿puedes analizar esta imagen?",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{encode_image_to_base64('./pngwing.png')}"
                }
            }
        ]
    }
]

response = client.chat.completions.create(
    model="gpt-4-o",
    messages=messages
)

print("REspuesta del analisis de la imagen")
print(response.choices[0].message.content)
