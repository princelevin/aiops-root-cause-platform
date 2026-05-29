from app.repositories.incident_repository import create_incident
from app.repositories.timeline_repository import create_timeline_event
from app.services.severity_service import calculate_severity, get_severity_reason


def build_incident_from_failure(failure: dict):
    severity = calculate_severity(
        failure_type=failure["failure_type"],
        latency_ms=failure["latency_ms"],
        service=failure["service"],
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
    incident = create_incident(db, incident_data)

    create_timeline_event(
        db,
        incident.id,
        "INCIDENT_CREATED",
        f"Incident created for {incident.service}",
    )

    create_timeline_event(
        db,
        incident.id,
        "FAILURE_DETECTED",
        failure["message"],
    )

    create_timeline_event(
        db,
        incident.id,
        "SEVERITY_ASSIGNED",
        f"Severity assigned as {incident.severity} - {get_severity_reason(incident.severity)}",
    )

    return incident