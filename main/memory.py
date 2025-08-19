# backend/memory.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
index_file = "backend/data/memory_index.faiss"
data_file = "backend/data/memory_data.pkl"

# Create data dir
os.makedirs("backend/data", exist_ok=True)

class VectorMemory:
    def __init__(self):
        self.embeddings = []
        self.metadata = []
        self.index = faiss.IndexFlatL2(384)  # 384 dim for MiniLM
        self.load()

    def add(self, text, metadata=None):
        emb = embedding_model.encode([text])
        self.index.add(emb)
        self.embeddings.append(emb[0])
        self.metadata.append(metadata or {})

    def search(self, query, k=3):
        q_emb = embedding_model.encode([query])
        scores, indices = self.index.search(q_emb, k)
        return [(self.metadata[i], float(scores[0][j])) for j, i in enumerate(indices[0])]

    def save(self):
        faiss.write_index(self.index, index_file)
        with open(data_file, 'wb') as f:
            pickle.dump((self.embeddings, self.metadata), f)

    def load(self):
        if os.path.exists(index_file) and os.path.exists(data_file):
            self.index = faiss.read_index(index_file)
            with open(data_file, 'rb') as f:
                self.embeddings, self.metadata = pickle.load(f)

# Global memory
memory = VectorMemory()