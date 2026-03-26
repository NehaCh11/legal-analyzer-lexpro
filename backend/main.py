from fastapi import FastAPI, Form
import requests

app = FastAPI()

def call_llm(prompt: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",  # or "mistral"
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

@app.post("/analyze/")
def analyze_legal(text: str = Form(...)):
    prompts = {
        "summary": (
            "Summarize the following legal document in clear language:\n\n"
            f"{text}"
        ),
        "clauses": (
            "Extract key clauses such as Termination, Liability, "
            "Jurisdiction, Payment, and Confidentiality:\n\n"
            f"{text}"
        ),
        "entities": (
            "Extract all named entities such as parties, dates, locations, "
            "laws, and monetary amounts:\n\n"
            f"{text}"
        )
    }

    results = {key: call_llm(prompt) for key, prompt in prompts.items()}
    return results
