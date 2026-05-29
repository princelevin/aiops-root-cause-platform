def calculate_severity(failure_type: str, latency_ms: int, service: str = ""):
    if failure_type == "payment_gateway_failure":
        return "P0"

    if failure_type == "db_pool_exhausted":
        return "P1"

    if failure_type == "redis_timeout":
        return "P1"

    if latency_ms >= 1000:
        return "P1"

    if latency_ms >= 700:
        return "P2"

    return "P3"


def get_severity_reason(severity: str):
    reasons = {
        "P0": "Critical business-impacting incident",
        "P1": "High priority production incident",
        "P2": "Medium severity performance degradation",
        "P3": "Low severity operational issue",
    }

    return reasons.get(severity, "Unknown severity")