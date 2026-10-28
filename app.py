from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI(title="LLM Deployment API")

# Load the pre-trained model and tokenizer once, when the application starts
MODEL_NAME = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


class PromptRequest(BaseModel):
    prompt: str


def run_inference(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    output_ids = model.generate(**inputs, max_new_tokens=50)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


@app.get("/")
def home():
    return {"message": "LLM API is running"}


@app.post("/generate")
def generate(request: PromptRequest):
    return {"response": run_inference(request.prompt)}