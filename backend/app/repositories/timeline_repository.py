from app.models.database_models import IncidentTimelineDB


def create_timeline_event(db, incident_id: int, event_type: str, description: str):
    event = IncidentTimelineDB(
        incident_id=incident_id,
        event_type=event_type,
        description=description,
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def get_timeline_by_incident(db, incident_id: int):
    return (
        db.query(IncidentTimelineDB)
        .filter(IncidentTimelineDB.incident_id == incident_id)
        .order_by(IncidentTimelineDB.id.asc())
        .all()
    )