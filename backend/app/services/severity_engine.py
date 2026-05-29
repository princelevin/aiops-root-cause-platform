def calculate_severity(failure: dict) -> str:
    latency = failure.get("latency_ms", 0)
    failure_type = failure.get("failure_type", "")
    service = failure.get("service", "")

    if failure_type == "payment_gateway_failure":
        return "P0"

    if failure_type == "db_pool_exhausted":
        return "P1"

    if failure_type == "redis_timeout" and latency >= 900:
        return "P1"

    if failure_type == "latency_spike":
        return "P2"

    if failure_type == "inventory_unavailable":
        return "P2"

    return "P3"