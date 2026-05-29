from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import ask_ollama


# APIs for sending raw text to the local AI model
router = APIRouter(prefix="/api/ai", tags=["Local AI"])


class AnalyzeRequest(BaseModel):
    # Text can be a log message, incident description, or failure message
    text: str


@router.post("/analyze")
def analyze_text(request: AnalyzeRequest):
    """
    Analyze any incident/log text using Ollama.
    """

    # Build the prompt for the local AI model
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

    # Send prompt to Ollama
    response = ask_ollama(prompt)

    # Return the original input and AI analysis
    return {
        "input": request.text,
        "analysis": response,
    }