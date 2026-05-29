from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.repositories.rca_repository import (
    save_rca_analysis,
    get_rca_history,
    get_rca_by_incident_id,
)
from app.services.rca_engine import analyze_root_cause

router = APIRouter(prefix="/api/rca", tags=["AI Root Cause Analysis"])


def rca_to_dict(rca):
    return {
        "id": rca.id,
        "incident_id": rca.incident_id,
        "service": rca.service,
        "severity": rca.severity,
        "failure_type": rca.failure_type,
        "root_cause": rca.root_cause,
        "recommendation": rca.recommendation,
        "confidence_score": rca.confidence_score,
        "created_at": rca.created_at,
    }


@router.get("")
def list_rca_history(db: Session = Depends(get_db)):
    history = get_rca_history(db)

    return {
        "rca_history": [rca_to_dict(item) for item in history]
    }


@router.get("/{incident_id}")
def get_root_cause_analysis(incident_id: int, db: Session = Depends(get_db)):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")

    analysis = analyze_root_cause(incident)
    saved_analysis = save_rca_analysis(db, analysis)

    return {
        "message": "Root cause analysis generated and saved successfully",
        "analysis": rca_to_dict(saved_analysis),
    }


@router.get("/incident/{incident_id}/latest")
def get_latest_rca_for_incident(incident_id: int, db: Session = Depends(get_db)):
    rca = get_rca_by_incident_id(db, incident_id)

    if rca is None:
        raise HTTPException(status_code=404, detail="RCA not found for this incident")

    return {
        "analysis": rca_to_dict(rca)
    }