from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter(prefix="/api/simulate", tags=["Simulation"])


@router.get("/payment")
def simulate_payment_service():
    latency = random.randint(80, 900)

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
    latency = random.randint(50, 500)

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
    stock_check = random.choice(["available", "low_stock", "unavailable"])

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