from openai import OpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
    
client = OpenAI(
    api_key=configure(),
)

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="O cachorro é um animal de estimação muito popular no Brasil.",
)

response.write_to_file('audio.mp3')