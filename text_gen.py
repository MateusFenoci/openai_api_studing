from openai import OpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
    
client = OpenAI(
    api_key=configure(),
)

input_user = input("Pergunte me qualquer capital do mundo: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", 
            "content": f"Você é um geógrafo especialista no país {input_user}"
        },
        {
            "role": "user", 
            "content": f"Qual a capital dos {input_user} e suas principais características geográficas?"
        },
    ],
    max_tokens=150,
    temperature=1,
)

if response.choices[0].message.content is not None:
    print(response.choices[0].message.content)