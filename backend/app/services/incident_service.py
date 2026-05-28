from datetime import datetime

incidents = []
incident_id_counter = 1


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


def create_incident_from_failure(failure: dict):
    global incident_id_counter

    severity = calculate_severity(
        failure_type=failure["failure_type"],
        latency_ms=failure["latency_ms"],
    )

    incident = {
        "id": incident_id_counter,
        "service": failure["service"],
        "title": failure["message"],
        "severity": severity,
        "status": "open",
        "root_cause_hint": failure["probable_cause"],
        "failure_type": failure["failure_type"],
        "latency_ms": failure["latency_ms"],
        "created_at": datetime.utcnow().isoformat(),
    }

    incidents.append(incident)
    incident_id_counter += 1

    return incident


def get_incidents():
    return incidents[-100:]


def get_incident_by_id(incident_id: int):
    for incident in incidents:
        if incident["id"] == incident_id:
            return incident

    return None