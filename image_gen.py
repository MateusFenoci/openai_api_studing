from openai import OpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")
    
client = OpenAI(
    api_key=configure(),
)

response = client.images.generate(
    model="dall-e-3",
    prompt="A imagem de um cachorro",
    size = "1024x1024",
    quality = "standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
## Output: https://oaidalleapiprodscus.blob.core.windows.net/private/org-lYn70x5DTblJBojc6YcBUHDs/user-6HfVX2P0PUusW7zA7ypmUopC/img-7hAmQfQhqS7T1QMvciEEIbov.png?st=2024-10-01T18%3A41%3A22Z&se=2024-10-01T20%3A41%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-30T21%3A21%3A19Z&ske=2024-10-01T21%3A21%3A19Z&sks=b&skv=2024-08-04&sig=FIAJz%2Bj7fmBWhgae%2BkQF5G2G4h7pgY6is8e6IzHVoX4%3D

