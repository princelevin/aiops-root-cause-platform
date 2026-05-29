from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.services.ai_rca_service import generate_ai_rca

router = APIRouter(prefix="/api/ai-rca", tags=["AI RCA"])


@router.get("/{incident_id}")
def get_ai_rca(incident_id: int, db: Session = Depends(get_db)):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    ai_response = generate_ai_rca(incident)

    return {
        "incident_id": incident_id,
        "ai_rca": ai_response,
    }