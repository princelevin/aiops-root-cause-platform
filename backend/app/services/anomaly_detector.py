from app.services.metrics_generator import get_metrics
from app.services.incident_service import create_incident_from_failure

LATENCY_THRESHOLD = 900
ERROR_RATE_THRESHOLD = 10.0
CPU_THRESHOLD = 85.0
MEMORY_THRESHOLD = 80.0


def incident_to_dict(incident):
    return {
        "id": incident.id,
        "service": incident.service,
        "title": incident.title,
        "severity": incident.severity,
        "status": incident.status,
        "root_cause_hint": incident.root_cause_hint,
        "failure_type": incident.failure_type,
        "latency_ms": incident.latency_ms,
        "created_at": incident.created_at,
    }


def detect_anomalies(db):
    metrics = get_metrics()
    detected_anomalies = []

    for metric in metrics:
        anomaly_reasons = []

        if metric["latency_ms"] >= LATENCY_THRESHOLD:
            anomaly_reasons.append("High latency detected")

        if metric["error_rate"] >= ERROR_RATE_THRESHOLD:
            anomaly_reasons.append("High error rate detected")

        if metric["cpu_usage"] >= CPU_THRESHOLD:
            anomaly_reasons.append("High CPU usage detected")

        if metric["memory_usage"] >= MEMORY_THRESHOLD:
            anomaly_reasons.append("High memory usage detected")

        if anomaly_reasons:
            failure = {
                "service": metric["service"],
                "level": "ERROR",
                "message": ", ".join(anomaly_reasons),
                "latency_ms": metric["latency_ms"],
                "failure_type": "metric_anomaly",
                "probable_cause": "Service exceeded operational metric thresholds",
                "timestamp": metric["timestamp"],
            }

            incident = create_incident_from_failure(db, failure)

            detected_anomalies.append({
                "metric": metric,
                "reasons": anomaly_reasons,
                "incident": incident_to_dict(incident),
            })

    return detected_anomalies