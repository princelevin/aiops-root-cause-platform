from fastapi import APIRouter


# APIs for showing services monitored by the platform
router = APIRouter(prefix="/api/services", tags=["Services"])


@router.get("")
def get_services():
    """
    Get all demo services.
    """

    # These are the fake microservices used in this AIOps demo
    return {
        "services": [
            {"name": "payment-service", "status": "healthy"},
            {"name": "order-service", "status": "healthy"},
            {"name": "inventory-service", "status": "healthy"},
        ]
    }