from app.models.database_models import IncidentDB


def create_incident(db, incident_data: dict):
    """
    Save a new incident in the database.
    """

    # Create IncidentDB object from incident data
    incident = IncidentDB(
        service=incident_data["service"],
        title=incident_data["title"],
        severity=incident_data["severity"],
        status=incident_data["status"],
        root_cause_hint=incident_data["root_cause_hint"],
        failure_type=incident_data["failure_type"],
        latency_ms=incident_data["latency_ms"],
    )

    # Save incident
    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def get_incidents(db):
    """
    Get all incidents, latest first.
    """

    return db.query(IncidentDB).order_by(IncidentDB.id.desc()).all()


def get_incident_by_id(db, incident_id: int):
    """
    Get one incident by ID.
    """

    return db.query(IncidentDB).filter(IncidentDB.id == incident_id).first()