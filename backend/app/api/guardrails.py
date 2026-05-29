from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.repositories.rca_repository import get_rca_by_incident_id
from app.services.guardrail_service import validate_ai_response

router = APIRouter(prefix="/api/guardrails", tags=["Guardrails"])


@router.get("/incident/{incident_id}")
def check_incident_guardrails(incident_id: int, db: Session = Depends(get_db)):
    incident = get_incident_by_id(db, incident_id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    rca = get_rca_by_incident_id(db, incident_id)

    if not rca:
        raise HTTPException(status_code=404, detail="RCA not found for this incident")

    context = {
        "service": incident.service,
        "severity": incident.severity,
        "failure_type": incident.failure_type,
        "root_cause_hint": incident.root_cause_hint,
        "root_cause": rca.root_cause,
        "recommendation": rca.recommendation,
    }

    ai_response = f"{rca.root_cause} {rca.recommendation}"

    result = validate_ai_response(context, ai_response)

    return {
        "incident_id": incident_id,
        "context_used": context,
        "ai_response_checked": ai_response,
        "guardrail_result": result,
    }