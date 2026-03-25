from openai import OpenAI
import os

USE_LOCAL = True  # switch between OpenAI and Ollama

if not USE_LOCAL:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate(prompt):
    if USE_LOCAL:
        import requests
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content