from fastapi import APIRouter

router = APIRouter(prefix="/api/services", tags=["Services"])


@router.get("")
def get_services():
    return {
        "services": [
            {"name": "payment-service", "status": "healthy"},
            {"name": "order-service", "status": "healthy"},
            {"name": "inventory-service", "status": "healthy"},
        ]
    }