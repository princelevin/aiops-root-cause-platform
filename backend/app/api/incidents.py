from fastapi import APIRouter

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])


@router.get("")
def get_incidents():
    return {
        "incidents": [
            {
                "id": 1,
                "service": "payment-service",
                "severity": "P1",
                "title": "High latency detected",
                "status": "open",
            }
        ]
    }