from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.services.rca_engine import analyze_root_cause

router = APIRouter(prefix="/api/rca", tags=["AI Root Cause Analysis"])


@router.get("/{incident_id}")
def get_root_cause_analysis(incident_id: int, db: Session = Depends(get_db)):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    analysis = analyze_root_cause(incident)

    return {
        "message": "Root cause analysis generated successfully",
        "analysis": analysis,
    }