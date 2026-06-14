from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import ask_helpdesk

app = FastAPI(title="IT Help Portal AI", version="2.0")

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"])

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(req: ChatRequest):
    answer = await ask_helpdesk(req.question)
    return {"answer": answer}

@app.get("/health")
def health():
    return {"status": "ok", "model": "llama3.2:1b"}
