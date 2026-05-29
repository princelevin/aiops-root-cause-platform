def analyze_root_cause(incident):
    failure_type = incident.failure_type
    service = incident.service
    latency = incident.latency_ms
    severity = incident.severity

    if failure_type == "redis_timeout":
        root_cause = "Redis connection timeout or Redis connection pool exhaustion"
        recommendation = "Check Redis availability, connection pool limits, and network latency between services."
        confidence = 0.92

    elif failure_type == "db_pool_exhausted":
        root_cause = "Database connection pool exhausted due to high concurrent requests"
        recommendation = "Increase DB pool size, optimize slow queries, and add request throttling."
        confidence = 0.9

    elif failure_type == "payment_gateway_failure":
        root_cause = "External payment provider outage or payment gateway timeout"
        recommendation = "Enable retry with exponential backoff and route traffic to fallback payment provider."
        confidence = 0.88

    elif failure_type == "metric_anomaly":
        if latency >= 900:
            root_cause = "High latency caused by service degradation or overloaded downstream dependency"
            recommendation = "Check service CPU, memory, downstream APIs, and recent deployments."
            confidence = 0.82
        else:
            root_cause = "Operational metric anomaly detected"
            recommendation = "Inspect service metrics, logs, and recent traffic spikes."
            confidence = 0.75

    else:
        root_cause = "Unknown operational failure pattern"
        recommendation = "Review logs, metrics, dependencies, and recent deployments."
        confidence = 0.6

    return {
        "incident_id": incident.id,
        "service": service,
        "severity": severity,
        "failure_type": failure_type,
        "root_cause": root_cause,
        "recommendation": recommendation,
        "confidence_score": confidence,
    }