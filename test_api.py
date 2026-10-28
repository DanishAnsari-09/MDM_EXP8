"""Sends the five lab prompts to the running API and prints a results table.
Run while the server is up (uvicorn or Docker):  python test_api.py
"""
import requests

URL = "https://mdm-exp8.onrender.com/generate"

prompts = [
    "What is artificial intelligence?",
    "Explain machine learning in simple words.",
    "What is a neural network?",
    "Explain the Transformer model.",
    "What is natural language processing?",
]

for i, p in enumerate(prompts, 1):
    r = requests.post(URL, json={"prompt": p}, timeout=120)
    r.raise_for_status()
    print(f"{i}. Prompt:   {p}")
    print(f"   Response: {r.json()['response']}\n")
