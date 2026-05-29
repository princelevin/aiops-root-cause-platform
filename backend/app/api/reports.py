from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.report_service import generate_incident_report


# APIs for generating incident reports
router = APIRouter(prefix="/api/reports", tags=["Reports"])


@router.get("/incident/{incident_id}")
def get_incident_report(
    incident_id: int,
    db: Session = Depends(get_db)
):
    """
    Generate report for one incident.
    """

    # Build report using incident, RCA, and timeline data
    report = generate_incident_report(db, incident_id)

    # Stop if incident does not exist
    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return {
        "message": "Incident report generated successfully",
        "report": report,
    }