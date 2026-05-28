from datetime import datetime
import random

logs = []
log_id_counter = 1


SERVICES = ["payment-service", "order-service", "inventory-service"]

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
    global log_id_counter

    service = random.choice(SERVICES)
    message = random.choice(LOG_MESSAGES[service])
    latency = random.randint(50, 1000)

    if "failed" in message.lower() or "timeout" in message.lower() or "exhausted" in message.lower():
        level = "ERROR"
    elif latency > 700 or "latency" in message.lower() or "delay" in message.lower():
        level = "WARN"
    else:
        level = "INFO"

    log = {
        "id": log_id_counter,
        "service": service,
        "level": level,
        "message": message,
        "latency_ms": latency,
        "timestamp": datetime.utcnow().isoformat(),
    }

    logs.append(log)
    log_id_counter += 1

    return log


def generate_logs(count: int = 10):
    return [generate_log() for _ in range(count)]


def get_logs():
    return logs[-100:]