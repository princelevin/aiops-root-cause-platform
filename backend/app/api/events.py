from fastapi import APIRouter
from app.services.event_queue import get_all_events, process_events

router = APIRouter(prefix="/api/events", tags=["Events"])


@router.get("")
def list_events():
    return {
        "events": get_all_events()
    }


@router.post("/process")
def process_event_queue():
    processed = process_events()

    return {
        "message": f"{len(processed)} events processed successfully",
        "processed_events": processed
    }