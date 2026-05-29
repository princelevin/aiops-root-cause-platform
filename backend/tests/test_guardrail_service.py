from app.services.guardrail_service import validate_ai_response


def test_guardrail_pass():
    context = {
        "service": "payment-service",
        "root_cause_hint": "Redis connection pool exhaustion",
    }

    response = (
        "Redis connection pool exhaustion detected. "
        "Check Redis availability."
    )

    result = validate_ai_response(context, response)

    assert result["is_grounded"] is True


def test_guardrail_fail():
    context = {
        "service": "payment-service",
        "root_cause_hint": "Redis connection pool exhaustion",
    }

    response = "Kubernetes cluster destroyed because of AWS outage."

    result = validate_ai_response(context, response)

    assert result["is_grounded"] is False