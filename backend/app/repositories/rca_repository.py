from app.models.database_models import RootCauseAnalysisDB


def save_rca_analysis(db, analysis: dict):
    rca = RootCauseAnalysisDB(
        incident_id=analysis["incident_id"],
        service=analysis["service"],
        severity=analysis["severity"],
        failure_type=analysis["failure_type"],
        root_cause=analysis["root_cause"],
        recommendation=analysis["recommendation"],
        confidence_score=analysis["confidence_score"],
    )

    db.add(rca)
    db.commit()
    db.refresh(rca)

    return rca


def get_rca_history(db):
    return (
        db.query(RootCauseAnalysisDB)
        .order_by(RootCauseAnalysisDB.id.desc())
        .all()
    )


def get_rca_by_incident_id(db, incident_id: int):
    return (
        db.query(RootCauseAnalysisDB)
        .filter(RootCauseAnalysisDB.incident_id == incident_id)
        .order_by(RootCauseAnalysisDB.id.desc())
        .first()
    )


# Needed by Day 24 Incident Report Generator
def get_latest_rca_by_incident_id(db, incident_id: int):
    return (
        db.query(RootCauseAnalysisDB)
        .filter(RootCauseAnalysisDB.incident_id == incident_id)
        .order_by(RootCauseAnalysisDB.id.desc())
        .first()
    )