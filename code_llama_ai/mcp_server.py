from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_engine.llama_interface import LlamaInterface

app = FastAPI()
llm = LlamaInterface()

class QueryRequest(BaseModel):
    query: str
    requirements: List[str] = []

@app.post("/query")
async def handle_query(request: QueryRequest):
    # Combine requirements into a context string
    context = ""
    if request.requirements:
        context = "Context from software requirements:\n" + "\n".join(request.requirements) + "\n\n"
    prompt = f"{context}You are an AI assistant. Answer the following question:\n{request.query}"
    response = llm.generate_response(prompt)
    return {"response": response} 