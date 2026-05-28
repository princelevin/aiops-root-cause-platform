from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import (
    get_incidents,
    get_incident_by_id,
)

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])


def incident_to_dict(incident):
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


@router.get("")
def list_incidents(db: Session = Depends(get_db)):
    incidents = get_incidents(db)
    return {"incidents": [incident_to_dict(i) for i in incidents]}


@router.get("/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return {"incident": incident_to_dict(incident)}