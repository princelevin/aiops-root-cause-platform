from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import ask_ollama

router = APIRouter(prefix="/api/ai", tags=["Local AI"])


class AnalyzeRequest(BaseModel):
    text: str


@router.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    prompt = f"""
You are an AIOps assistant.

Analyze the following production incident/log and explain:
1. Likely root cause
2. Impacted service
3. Recommended fix

Text:
{request.text}

Keep the answer short and practical.
"""

    response = ask_ollama(prompt)

    return {
        "input": request.text,
        "analysis": response,
    }