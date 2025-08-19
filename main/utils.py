# utils.py
import pandas as pd
import numpy as np
import dateparser
from datetime import datetime, timedelta
import os
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ——————————————————————
# Global Embedding Model
# ——————————————————————
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# ——————————————————————
# Text & Date Helpers
# ——————————————————————
def extract_date(text):
    """Extract date from string"""
    return dateparser.parse(str(text))

def contains_keywords(text, keywords):
    """Check if text contains any keyword"""
    text = str(text).lower()
    return any(k.lower() in text for k in keywords)

# ——————————————————————
# Embedding & Similarity
# ——————————————————————
def get_embeddings(texts):
    """Get embeddings for list of texts or single string"""
    if isinstance(texts, str):
        texts = [texts]
    return embedding_model.encode(texts)

def find_similar(items, query, top_k=3):
    """Find most similar items using cosine similarity"""
    if not items:
        return []
    item_embeddings = get_embeddings(items)
    query_embedding = get_embeddings(query)
    sims = cosine_similarity(query_embedding, item_embeddings)[0]
    indices = sims.argsort()[-top_k:][::-1]
    return [(items[i], float(sims[i])) for i in indices]

# ——————————————————————
# Data Saving / Loading
# ——————————————————————
def save_pickle(obj, filepath):
    """Save object to pickle"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)

def load_pickle(filepath):
    """Load object from pickle, return None if not found"""
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    return None

# ——————————————————————
# Tone Templates for Rewriting (Fallback)
# ——————————————————————
def generate_tone_prompt(text, tone):
    tone_map = {
        "professional": f"Make this professional and concise: {text}",
        "friendly": f"Rewrite in a warm, friendly tone: {text}",
        "urgent": f"Make this urgent and action-oriented: {text}",
        "apology": f"Rewrite as a sincere apology: {text}",
        "excited": f"Rewrite with excitement and enthusiasm: {text}"
    }
    return tone_map.get(tone.lower(), f"Rewrite in {tone} tone: {text}")