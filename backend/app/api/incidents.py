from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import (
    get_incidents,
    get_incident_by_id,
)
from app.repositories.timeline_repository import get_timeline_by_incident


# APIs for viewing incidents and incident timelines
router = APIRouter(prefix="/api/incidents", tags=["Incidents"])


def incident_to_dict(incident):
    # Convert DB incident object into JSON response
    return {
        "id": incident.id,
        "service": incident.service,
        "title": incident.title,
        "severity": incident.severity,
        "status": incident.status,
        "root_cause_hint": incident.root_cause_hint,
        "failure_type": incident.failure_type,
        "latency_ms": incident.latency_ms,
        "created_at": incident.created_at,
    }


def timeline_to_dict(event):
    # Convert DB timeline object into JSON response
    return {
        "id": event.id,
        "incident_id": event.incident_id,
        "event_type": event.event_type,
        "description": event.description,
        "timestamp": event.timestamp,
    }


@router.get("")
def list_incidents(db: Session = Depends(get_db)):
    """
    Get all incidents.
    """

    incidents = get_incidents(db)

    return {
        "incidents": [incident_to_dict(i) for i in incidents]
    }


@router.get("/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    """
    Get one incident by ID.
    """

    incident = get_incident_by_id(db, incident_id)

    # Stop if incident does not exist
    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return {
        "incident": incident_to_dict(incident)
    }


@router.get("/{incident_id}/timeline")
def get_incident_timeline(incident_id: int, db: Session = Depends(get_db)):
    """
    Get timeline events for one incident.
    """

    incident = get_incident_by_id(db, incident_id)

    # Stop if incident does not exist
    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    timeline = get_timeline_by_incident(db, incident_id)

    return {
        "incident": incident_to_dict(incident),
        "timeline": [timeline_to_dict(event) for event in timeline],
    }