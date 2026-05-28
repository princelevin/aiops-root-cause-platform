from fastapi import APIRouter, HTTPException
from app.services.incident_service import get_incidents, get_incident_by_id

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])


@router.get("")
def list_incidents():
    return {"incidents": get_incidents()}


@router.get("/{incident_id}")
def get_incident(incident_id: int):
    incident = get_incident_by_id(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return {"incident": incident}