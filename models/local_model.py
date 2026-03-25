import requests
from config import MODEL_NAME, OLLAMA_URL

def generate(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json().get("response", "")