import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

MEMORY_FILE = "memory/chat_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_interaction(query, response):
    memory = load_memory()

    embedding = model.encode([query])[0].tolist()

    memory.append({
        "query": query,
        "response": response,
        "embedding": embedding
    })

    save_memory(memory)

def get_similar_queries(query, top_k=2):
    memory = load_memory()
    if not memory:
        return []

    query_vec = model.encode([query])[0]

    scores = []
    for item in memory:
        mem_vec = np.array(item["embedding"])
        score = np.dot(query_vec, mem_vec)
        scores.append(score)

    top_idx = np.argsort(scores)[-top_k:]

    return [memory[i] for i in top_idx]