from app.services.ollama_service import ask_ollama


def generate_ai_rca(incident):
    """
    Generate AI RCA for one incident.
    """

    # Build prompt using incident details
    prompt = f"""
You are an expert AIOps root cause analysis assistant.

Analyze this incident:

Incident ID: {incident.id}
Service: {incident.service}
Severity: {incident.severity}
Failure Type: {incident.failure_type}
Title: {incident.title}
Latency: {incident.latency_ms} ms
Existing Hint: {incident.root_cause_hint}

Return a short structured response with:
- Root Cause
- Impact
- Recommended Fix
- Confidence from 0 to 100

Be practical and concise.
"""

    # Send prompt to local Ollama model
    return ask_ollama(prompt)