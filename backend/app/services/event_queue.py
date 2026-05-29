from datetime import datetime
from typing import List, Dict


# In-memory event queue for demo purposes
event_queue: List[Dict] = []


def publish_event(event_type: str, payload: dict):
    """
    Add a new event to the queue.
    """

    # Create event object
    event = {
        "id": len(event_queue) + 1,
        "event_type": event_type,
        "payload": payload,
        "status": "queued",
        "created_at": datetime.utcnow().isoformat()
    }

    # Store event in queue
    event_queue.append(event)

    return event


def get_all_events():
    """
    Get all events from the queue.
    """

    return event_queue


def process_events():
    """
    Mark all queued events as processed.
    """

    processed = []

    for event in event_queue:

        # Process only events that are still queued
        if event["status"] == "queued":
            event["status"] = "processed"
            event["processed_at"] = datetime.utcnow().isoformat()
            processed.append(event)

    return processed