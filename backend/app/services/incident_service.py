from app.repositories.incident_repository import create_incident


def calculate_severity(failure_type: str, latency_ms: int):
    if failure_type == "payment_gateway_failure":
        return "P0"

    if failure_type in ["redis_timeout", "db_pool_exhausted"]:
        return "P1"

    if latency_ms >= 900:
        return "P1"

    if latency_ms >= 700:
        return "P2"

    return "P3"


def build_incident_from_failure(failure: dict):
    severity = calculate_severity(
        failure_type=failure["failure_type"],
        latency_ms=failure["latency_ms"],
    )

    return {
        "service": failure["service"],
        "title": failure["message"],
        "severity": severity,
        "status": "open",
        "root_cause_hint": failure["probable_cause"],
        "failure_type": failure["failure_type"],
        "latency_ms": failure["latency_ms"],
    }


def create_incident_from_failure(db, failure: dict):
    incident_data = build_incident_from_failure(failure)
    return create_incident(db, incident_data)