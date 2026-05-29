def correlate_incidents(target_incident, all_incidents):
    related = []

    for incident in all_incidents:
        if incident.id == target_incident.id:
            continue

        score = 0
        reasons = []

        if incident.service == target_incident.service:
            score += 35
            reasons.append("Same affected service")

        if incident.failure_type == target_incident.failure_type:
            score += 30
            reasons.append("Same failure type")

        if incident.root_cause_hint == target_incident.root_cause_hint:
            score += 25
            reasons.append("Same root cause hint")

        if incident.severity == target_incident.severity:
            score += 10
            reasons.append("Same severity level")

        if score >= 30:
            related.append({
                "incident_id": incident.id,
                "service": incident.service,
                "title": incident.title,
                "severity": incident.severity,
                "status": incident.status,
                "failure_type": incident.failure_type,
                "correlation_score": score,
                "reasons": reasons,
            })

    related.sort(key=lambda item: item["correlation_score"], reverse=True)

    return related