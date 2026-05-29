from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.incident_repository import get_incident_by_id
from app.repositories.rca_repository import get_rca_by_incident_id
from app.services.guardrail_service import validate_ai_response


# APIs for checking whether AI RCA is grounded in incident data
router = APIRouter(prefix="/api/guardrails", tags=["Guardrails"])


@router.get("/incident/{incident_id}")
def check_incident_guardrails(
    incident_id: int,
    db: Session = Depends(get_db)
):
    """
    Validate AI RCA for a specific incident.
    """

    # Get incident details
    incident = get_incident_by_id(db, incident_id)

    # Stop if incident does not exist
    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    # Get latest RCA for the incident
    rca = get_rca_by_incident_id(db, incident_id)

    # Stop if RCA has not been generated yet
    if not rca:
        raise HTTPException(
            status_code=404,
            detail="RCA not found for this incident"
        )

    # Build context used for validation
    context = {
        "service": incident.service,
        "severity": incident.severity,
        "failure_type": incident.failure_type,
        "root_cause_hint": incident.root_cause_hint,
        "root_cause": rca.root_cause,
        "recommendation": rca.recommendation,
    }

    # Combine RCA output into one response
    ai_response = f"{rca.root_cause} {rca.recommendation}"

    # Check whether AI response matches incident context
    result = validate_ai_response(context, ai_response)

    return {
        "incident_id": incident_id,
        "context_used": context,
        "ai_response_checked": ai_response,
        "guardrail_result": result,
    }