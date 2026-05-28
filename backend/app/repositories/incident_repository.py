from app.models.database_models import IncidentDB


def create_incident(db, incident_data: dict):
    incident = IncidentDB(
        service=incident_data["service"],
        title=incident_data["title"],
        severity=incident_data["severity"],
        status=incident_data["status"],
        root_cause_hint=incident_data["root_cause_hint"],
        failure_type=incident_data["failure_type"],
        latency_ms=incident_data["latency_ms"],
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def get_incidents(db):
    return db.query(IncidentDB).order_by(IncidentDB.id.desc()).all()


def get_incident_by_id(db, incident_id: int):
    return db.query(IncidentDB).filter(IncidentDB.id == incident_id).first()