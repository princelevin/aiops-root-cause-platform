from fastapi import APIRouter

from app.services.event_queue import get_all_events, process_events


# APIs for viewing and processing internal events
router = APIRouter(prefix="/api/events", tags=["Events"])


@router.get("")
def list_events():
    """
    Get all queued and processed events.
    """

    # Return current event queue
    return {
        "events": get_all_events()
    }


@router.post("/process")
def process_event_queue():
    """
    Process all queued events.
    """

    # Mark queued events as processed
    processed = process_events()

    # Return processed event details
    return {
        "message": f"{len(processed)} events processed successfully",
        "processed_events": processed
    }