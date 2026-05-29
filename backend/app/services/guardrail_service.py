def validate_ai_response(context: dict, ai_response: str):
    """
    Check if AI response is based on given incident context.
    """

    allowed_keywords = []

    # Collect context values that AI is allowed to use
    for key, value in context.items():
        if value:
            allowed_keywords.append(str(value).lower())

    response_lower = ai_response.lower()

    # Check which context values are present in AI response
    matched_keywords = [
        keyword for keyword in allowed_keywords
        if keyword in response_lower
    ]

    # If at least one context value matched, we treat it as grounded
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