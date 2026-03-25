from sentence_transformers import SentenceTransformer
import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.docs = []
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.vectors = []

    def add(self, text):
        self.docs.append(text)
        embedding = self.model.encode(text)
        self.vectors.append(embedding)

    def search(self, query, k=2):
        if not self.docs:
            return []

        q_vec = self.model.encode(query)

        sims = [
            np.dot(q_vec, doc_vec) / (np.linalg.norm(q_vec) * np.linalg.norm(doc_vec))
            for doc_vec in self.vectors
        ]

        top_idx = np.argsort(sims)[-k:][::-1]

        return [self.docs[i] for i in top_idx]