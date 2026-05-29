from app.models.database_models import RootCauseAnalysisDB


def save_rca_analysis(db, analysis: dict):
    """
    Save RCA result in the database.
    """

    # Create RCA DB object
    rca = RootCauseAnalysisDB(
        incident_id=analysis["incident_id"],
        service=analysis["service"],
        severity=analysis["severity"],
        failure_type=analysis["failure_type"],
        root_cause=analysis["root_cause"],
        recommendation=analysis["recommendation"],
        confidence_score=analysis["confidence_score"],
    )

    # Save RCA result
    db.add(rca)
    db.commit()
    db.refresh(rca)

    return rca


def get_rca_history(db):
    """
    Get all RCA results, latest first.
    """

    return (
        db.query(RootCauseAnalysisDB)
        .order_by(RootCauseAnalysisDB.id.desc())
        .all()
    )


def get_rca_by_incident_id(db, incident_id: int):
    """
    Get latest RCA for one incident.
    """

    return (
        db.query(RootCauseAnalysisDB)
        .filter(RootCauseAnalysisDB.incident_id == incident_id)
        .order_by(RootCauseAnalysisDB.id.desc())
        .first()
    )


def get_latest_rca_by_incident_id(db, incident_id: int):
    """
    Same as get_rca_by_incident_id.
    Used by report generation.
    """

    return get_rca_by_incident_id(db, incident_id)