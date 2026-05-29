from fastapi import APIRouter
from datetime import datetime
import random


# APIs for simulating fake microservice responses
router = APIRouter(prefix="/api/simulate", tags=["Simulation"])


@router.get("/payment")
def simulate_payment_service():
    """
    Simulate payment-service behavior.
    """

    # Generate random latency to mimic real service response time
    latency = random.randint(80, 900)

    # Mark service as degraded if latency is high
    if latency > 600:
        status = "degraded"
        message = "Payment service latency spike detected"
    else:
        status = "healthy"
        message = "Payment processed successfully"

    return {
        "service": "payment-service",
        "status": status,
        "latency_ms": latency,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/order")
def simulate_order_service():
    """
    Simulate order-service behavior.
    """

    # Generate random latency for order service
    latency = random.randint(50, 500)

    # Mark service as degraded if response time is slow
    if latency > 350:
        status = "degraded"
        message = "Order service response delay detected"
    else:
        status = "healthy"
        message = "Order created successfully"

    return {
        "service": "order-service",
        "status": status,
        "latency_ms": latency,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/inventory")
def simulate_inventory_service():
    """
    Simulate inventory-service behavior.
    """

    # Randomly simulate inventory states
    stock_check = random.choice(["available", "low_stock", "unavailable"])

    # Convert inventory state into service status
    if stock_check == "unavailable":
        status = "error"
        message = "Inventory unavailable for requested item"
    elif stock_check == "low_stock":
        status = "degraded"
        message = "Inventory running low"
    else:
        status = "healthy"
        message = "Inventory check successful"

    return {
        "service": "inventory-service",
        "status": status,
        "stock_status": stock_check,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }