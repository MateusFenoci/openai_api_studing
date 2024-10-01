from openai import OpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
    
client = OpenAI(
    api_key=configure(),
)

audio_file = open("audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model= "whisper-1",
    file= audio_file,
    response_format= "text"
)

print(transcription)