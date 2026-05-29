def calculate_severity(failure_type: str, latency_ms: int, service: str = ""):
    """
    Calculate incident severity.
    """

    # Payment failures directly affect users/business
    if failure_type == "payment_gateway_failure":
        return "P0"

    # Database issues are high priority
    if failure_type == "db_pool_exhausted":
        return "P1"

    # Redis timeout can break payment/session flow
    if failure_type == "redis_timeout":
        return "P1"

    # Very high latency is treated as high priority
    if latency_ms >= 900:
        return "P1"

    # Medium latency degradation
    if latency_ms >= 700:
        return "P2"

    # Default low priority
    return "P3"


def get_severity_reason(severity: str):
    """
    Explain severity in simple words.
    """

    reasons = {
        "P0": "Critical business-impacting incident",
        "P1": "High priority production incident",
        "P2": "Medium severity performance degradation",
        "P3": "Low severity operational issue",
    }

    return reasons.get(severity, "Unknown severity")