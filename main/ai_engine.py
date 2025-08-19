# backend/ai_engine.py
from transformers import pipeline, T5ForConditionalGeneration, T5Tokenizer
import torch

# Load T5 for text generation
model_name = "t5-small"  # Use "google/flan-t5-base" if you want better quality
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
device = 0 if torch.cuda.is_available() else -1

summarizer = pipeline("summarization", model=model_name, tokenizer=model_name, device=device)
rephraser = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=device)

def summarize(text, max_length=100):
    if len(text.split()) < 20:
        return text
    return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

def rewrite(text, tone="professional"):
    prompt = f"Rewrite in {tone} tone: {text}"
    return rephraser(prompt, max_length=100)[0]['generated_text']