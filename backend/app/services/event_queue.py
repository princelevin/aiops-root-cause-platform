from datetime import datetime
from typing import List, Dict

event_queue: List[Dict] = []


def publish_event(event_type: str, payload: dict):
    event = {
        "id": len(event_queue) + 1,
        "event_type": event_type,
        "payload": payload,
        "status": "queued",
        "created_at": datetime.utcnow().isoformat()
    }

    event_queue.append(event)
    return event


def get_all_events():
    return event_queue


def process_events():
    processed = []

    for event in event_queue:
        if event["status"] == "queued":
            event["status"] = "processed"
            event["processed_at"] = datetime.utcnow().isoformat()
            processed.append(event)

    return processed