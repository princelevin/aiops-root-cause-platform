from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import (
    get_incident_by_id,
    get_incidents,
)
from app.services.correlation_engine import correlate_incidents

router = APIRouter(prefix="/api/correlation", tags=["Incident Correlation"])


@router.get("/{incident_id}")
def get_incident_correlations(incident_id: int, db: Session = Depends(get_db)):
    target_incident = get_incident_by_id(db, incident_id)

    if target_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    all_incidents = get_incidents(db)
    related_incidents = correlate_incidents(target_incident, all_incidents)

    return {
        "incident_id": incident_id,
        "related_incidents_count": len(related_incidents),
        "related_incidents": related_incidents,
    }