from app.repositories.incident_repository import get_incident_by_id
from app.repositories.timeline_repository import get_timeline_events_by_incident_id
from app.repositories.rca_repository import get_latest_rca_by_incident_id


def generate_incident_report(db, incident_id: int):
    incident = get_incident_by_id(db, incident_id)

    if not incident:
        return None

    timeline = get_timeline_events_by_incident_id(db, incident_id)    
    rca = get_latest_rca_by_incident_id(db, incident_id)

    report = {
        "incident_id": incident.id,
        "service": incident.service,
        "severity": incident.severity,
        "status": incident.status,
        "title": incident.title,
        "failure_type": incident.failure_type,
        "latency_ms": incident.latency_ms,
        "root_cause_hint": incident.root_cause_hint,
        "created_at": incident.created_at,
        "rca": {
            "root_cause": rca.root_cause if rca else "RCA not generated yet",
            "recommendation": rca.recommendation if rca else "No recommendation available",
            "confidence_score": rca.confidence_score if rca else None,
        },
        "timeline": [
            {
                "event_type": item.event_type,
                "description": item.description,
                "timestamp": item.timestamp,
            }
            for item in timeline
        ],
        "summary": f"{incident.severity} incident detected in {incident.service}. Root cause hint: {incident.root_cause_hint}.",
    }

    return report