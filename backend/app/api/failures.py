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


# APIs for injecting fake production failures
router = APIRouter(prefix="/api/failures", tags=["Failures"])


@router.get("/scenarios")
def list_failure_scenarios():
    """
    Show all failure types supported by the system.
    """

    return {
        "scenarios": get_failure_scenarios()
    }


@router.post("/inject/{failure_type}")
def create_failure(
    failure_type: str,
    db: Session = Depends(get_db)
):
    """
    Inject a failure and create an incident from it.
    """

    # Create fake failure based on selected type
    failure = inject_failure(failure_type)

    # Stop if invalid failure type is passed
    if failure is None:
        raise HTTPException(
            status_code=404,
            detail="Failure type not found",
        )

    # Convert failure into incident
    incident = create_incident_from_failure(db, failure)

    # Prepare incident response payload
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

    # Add incident-created event to queue
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
    """
    Show all generated failures.
    """

    return {
        "failures": get_failures()
    }