from datetime import datetime


# Simple in-memory storage for generated failures
failure_id_counter = 1
failures = []


# Predefined failure scenarios used for demo/testing
FAILURE_SCENARIOS = {
    "redis_timeout": {
        "service": "payment-service",
        "level": "ERROR",
        "message": "Redis timeout while validating payment session",
        "latency_ms": 950,
        "failure_type": "redis_timeout",
        "probable_cause": "Redis connection pool exhaustion",
    },
    "db_pool_exhausted": {
        "service": "order-service",
        "level": "ERROR",
        "message": "Database connection pool exhausted",
        "latency_ms": 880,
        "failure_type": "db_pool_exhausted",
        "probable_cause": "Too many concurrent database connections",
    },
    "payment_gateway_failure": {
        "service": "payment-service",
        "level": "ERROR",
        "message": "Payment failed due to downstream provider error",
        "latency_ms": 720,
        "failure_type": "payment_gateway_failure",
        "probable_cause": "External payment provider outage",
    },
    "inventory_unavailable": {
        "service": "inventory-service",
        "level": "ERROR",
        "message": "Inventory unavailable for requested item",
        "latency_ms": 500,
        "failure_type": "inventory_unavailable",
        "probable_cause": "Inventory service returned unavailable stock state",
    },
    "latency_spike": {
        "service": "order-service",
        "level": "WARN",
        "message": "Order service response delay detected",
        "latency_ms": 1100,
        "failure_type": "latency_spike",
        "probable_cause": "High request latency due to overloaded service",
    },
}


def inject_failure(failure_type: str):
    """
    Create one fake failure based on selected scenario.
    """

    global failure_id_counter

    # Stop if unsupported failure type is passed
    if failure_type not in FAILURE_SCENARIOS:
        return None

    scenario = FAILURE_SCENARIOS[failure_type]

    # Build failure object from scenario data
    failure = {
        "id": failure_id_counter,
        "service": scenario["service"],
        "level": scenario["level"],
        "message": scenario["message"],
        "latency_ms": scenario["latency_ms"],
        "failure_type": scenario["failure_type"],
        "probable_cause": scenario["probable_cause"],
        "timestamp": datetime.utcnow().isoformat(),
    }

    # Save failure in memory
    failures.append(failure)
    failure_id_counter += 1

    return failure


def get_failures():
    """
    Return latest generated failures.
    """

    return failures[-100:]


def get_failure_scenarios():
    """
    Return supported failure scenario names.
    """

    return list(FAILURE_SCENARIOS.keys())