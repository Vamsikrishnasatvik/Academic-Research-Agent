from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

memory_vectors = []
memory_texts = []

def store_memory(text):
    vec = model.encode([text])[0]
    memory_vectors.append(vec)
    memory_texts.append(text)

def retrieve_memory(query):
    if not memory_vectors:
        return []

    query_vec = model.encode([query])[0]
    scores = np.dot(memory_vectors, query_vec)

    top_idx = np.argsort(scores)[-2:]
    return [memory_texts[i] for i in top_idx]