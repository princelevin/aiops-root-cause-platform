from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.services.ai_rca_service import generate_ai_rca


# APIs for AI-based root cause analysis
router = APIRouter(
    prefix="/api/ai-rca",
    tags=["AI RCA"]
)


@router.get("/{incident_id}")
def get_ai_rca(
    incident_id: int,
    db: Session = Depends(get_db)
):
    """
    Generate AI RCA for one incident.
    """

    # Get incident from DB
    incident = get_incident_by_id(db, incident_id)

    # Stop if incident does not exist
    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    # Ask local AI model to analyze the incident
    ai_response = generate_ai_rca(incident)

    # Send AI RCA result back
    return {
        "incident_id": incident_id,
        "ai_rca": ai_response,
    }