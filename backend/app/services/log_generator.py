from datetime import datetime
import random


# In-memory storage for generated logs
logs = []
log_id_counter = 1


# Demo services used in the platform
SERVICES = ["payment-service", "order-service", "inventory-service"]


# Sample log messages for each service
LOG_MESSAGES = {
    "payment-service": [
        "Payment processed successfully",
        "Payment gateway timeout",
        "Redis timeout while validating payment session",
        "High latency detected in payment authorization",
        "Payment failed due to downstream provider error",
    ],
    "order-service": [
        "Order created successfully",
        "Order validation completed",
        "Order service response delay detected",
        "Database connection pool exhausted",
        "Failed to create order due to inventory dependency",
    ],
    "inventory-service": [
        "Inventory check successful",
        "Inventory running low",
        "Inventory unavailable for requested item",
        "Warehouse lookup latency spike",
        "Failed to reserve inventory",
    ],
}


def generate_log():
    """
    Generate one fake service log.
    """

    global log_id_counter

    service = random.choice(SERVICES)
    message = random.choice(LOG_MESSAGES[service])
    latency = random.randint(50, 1000)

    # Decide log level based on message and latency
    if "failed" in message.lower() or "timeout" in message.lower() or "exhausted" in message.lower():
        level = "ERROR"
    elif latency > 700 or "latency" in message.lower() or "delay" in message.lower():
        level = "WARN"
    else:
        level = "INFO"

    # Build log object
    log = {
        "id": log_id_counter,
        "service": service,
        "level": level,
        "message": message,
        "latency_ms": latency,
        "timestamp": datetime.utcnow().isoformat(),
    }

    # Store log in memory
    logs.append(log)
    log_id_counter += 1

    return log


def generate_logs(count: int = 10):
    """
    Generate multiple fake logs.
    """

    return [generate_log() for _ in range(count)]


def get_logs():
    """
    Return latest generated logs.
    """

    return logs[-100:]