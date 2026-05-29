from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.event_queue import publish_event
from app.services.failure_injector import (
    inject_failure,
    get_failures,
    get_failure_scenarios,
)
from app.services.incident_service import create_incident_from_failure

router = APIRouter(prefix="/api/failures", tags=["Failures"])


@router.get("/scenarios")
def list_failure_scenarios():
    return {"scenarios": get_failure_scenarios()}


@router.post("/inject/{failure_type}")
def create_failure(failure_type: str, db: Session = Depends(get_db)):
    failure = inject_failure(failure_type)

    if failure is None:
        raise HTTPException(
            status_code=404,
            detail="Failure type not found",
        )

    incident = create_incident_from_failure(db, failure)

    incident_payload = {
        "id": incident.id,
        "service": incident.service,
        "title": incident.title,
        "severity": incident.severity,
        "status": incident.status,
        "root_cause_hint": incident.root_cause_hint,
        "failure_type": incident.failure_type,
        "latency_ms": incident.latency_ms,
        "created_at": str(incident.created_at),
    }

    publish_event(
        event_type="INCIDENT_CREATED",
        payload=incident_payload,
    )

    return {
        "message": "Failure injected, incident created, and event published successfully",
        "failure": failure,
        "incident": incident_payload,
    }


@router.get("")
def list_failures():
    return {"failures": get_failures()}