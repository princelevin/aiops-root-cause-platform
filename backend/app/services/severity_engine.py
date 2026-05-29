def calculate_severity(failure: dict) -> str:
    """
    Calculate severity from failure details.
    """

    latency = failure.get("latency_ms", 0)
    failure_type = failure.get("failure_type", "")

    # Payment failures are business critical
    if failure_type == "payment_gateway_failure":
        return "P0"

    # DB connection issues are high priority
    if failure_type == "db_pool_exhausted":
        return "P1"

    # Redis timeout with high latency is high priority
    if failure_type == "redis_timeout" and latency >= 900:
        return "P1"

    # Latency spike is medium priority
    if failure_type == "latency_spike":
        return "P2"

    # Inventory unavailable is medium priority
    if failure_type == "inventory_unavailable":
        return "P2"

    # Default severity for low impact issues
    return "P3"