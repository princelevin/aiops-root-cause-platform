from app.models.database_models import IncidentTimelineDB


def create_timeline_event(db, incident_id: int, event_type: str, description: str):
    """
    Save one timeline event for an incident.
    """

    # Create timeline event
    event = IncidentTimelineDB(
        incident_id=incident_id,
        event_type=event_type,
        description=description,
    )

    # Save event
    db.add(event)
    db.commit()
    db.refresh(event)

    return event


def get_timeline_by_incident(db, incident_id: int):
    """
    Get all timeline events for one incident.
    """

    return (
        db.query(IncidentTimelineDB)
        .filter(IncidentTimelineDB.incident_id == incident_id)
        .order_by(IncidentTimelineDB.id.asc())
        .all()
    )


def get_timeline_events_by_incident_id(db, incident_id: int):
    """
    Alias used by report service.
    """

    return get_timeline_by_incident(db, incident_id)