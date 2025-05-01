from fastapi import APIRouter, Body
from agents.langchain_agent import run_agent
from backend.service.chat_service import answer_query

router = APIRouter()

@router.post("/chat")
def chat(input: dict = Body(...)):
    response = answer_query(input.get("message", ""))
    return {"response": response}
