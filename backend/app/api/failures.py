from fastapi import APIRouter, HTTPException
from app.services.failure_injector import (
    inject_failure,
    get_failures,
    get_failure_scenarios,
)
from app.services.incident_service import create_incident_from_failure

router = APIRouter(prefix="/api/failures", tags=["Failures"])


@router.get("/scenarios")
def list_failure_scenarios():
    return {"scenarios": get_failure_scenarios()}


@router.post("/inject/{failure_type}")
def create_failure(failure_type: str):
    failure = inject_failure(failure_type)

    if failure is None:
        raise HTTPException(
            status_code=404,
            detail="Failure type not found",
        )

    incident = create_incident_from_failure(failure)

    return {
        "message": "Failure injected and incident created successfully",
        "failure": failure,
        "incident": incident,
    }


@router.get("")
def list_failures():
    return {"failures": get_failures()}