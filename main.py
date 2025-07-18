from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
import requests

app = FastAPI()

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_ai(q: Question):
    # Xử lý AI (ví dụ: gọi model Ollama)
    response = client.chat.completions.create(
        model="deepseek-r1:8b",
        messages=[
            {"role": "user", "content": q.question} 
        ]
    )
    reply = response.choices[0].message.content
    return {"answer": reply}
