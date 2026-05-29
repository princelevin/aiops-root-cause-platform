def correlate_incidents(target_incident, all_incidents):
    """
    Find incidents that are similar to the selected incident.
    """

    related = []

    for incident in all_incidents:

        # Skip comparing the incident with itself
        if incident.id == target_incident.id:
            continue

        score = 0
        reasons = []

        # Same service increases correlation score
        if incident.service == target_incident.service:
            score += 35
            reasons.append("Same affected service")

        # Same failure type increases correlation score
        if incident.failure_type == target_incident.failure_type:
            score += 30
            reasons.append("Same failure type")

        # Same root cause hint increases correlation score
        if incident.root_cause_hint == target_incident.root_cause_hint:
            score += 25
            reasons.append("Same root cause hint")

        # Same severity increases correlation score
        if incident.severity == target_incident.severity:
            score += 10
            reasons.append("Same severity level")

        # Only keep incidents with meaningful correlation
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

    # Show highest correlated incidents first
    related.sort(
        key=lambda item: item["correlation_score"],
        reverse=True
    )

    return related