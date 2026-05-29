def validate_ai_response(context: dict, ai_response: str):
    allowed_keywords = []

    for key, value in context.items():
        if value:
            allowed_keywords.append(str(value).lower())

    response_lower = ai_response.lower()

    matched_keywords = [
        keyword for keyword in allowed_keywords
        if keyword in response_lower
    ]

    is_grounded = len(matched_keywords) > 0

    return {
        "is_grounded": is_grounded,
        "matched_context": matched_keywords,
        "guardrail_status": "PASSED" if is_grounded else "FAILED",
        "message": (
            "AI response is grounded in incident context"
            if is_grounded
            else "AI response may contain unsupported information"
        ),
    }