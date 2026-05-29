from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import (
    get_incident_by_id,
    get_incidents,
)
from app.services.correlation_engine import correlate_incidents


# APIs for finding incidents related to a selected incident
router = APIRouter(prefix="/api/correlation", tags=["Incident Correlation"])


@router.get("/{incident_id}")
def get_incident_correlations(
    incident_id: int,
    db: Session = Depends(get_db)
):
    """
    Find incidents similar to the selected incident.
    """

    # Get selected incident from DB
    target_incident = get_incident_by_id(db, incident_id)

    # Stop if incident does not exist
    if target_incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    # Get all incidents to compare against
    all_incidents = get_incidents(db)

    # Find related incidents using correlation logic
    related_incidents = correlate_incidents(target_incident, all_incidents)

    # Return related incidents with score and reasons
    return {
        "incident_id": incident_id,
        "related_incidents_count": len(related_incidents),
        "related_incidents": related_incidents,
    }