from fastapi import APIRouter, Query
from app.services.log_generator import generate_logs, get_logs

router = APIRouter(prefix="/api/logs", tags=["Logs"])


@router.get("")
def list_logs():
    return {"logs": get_logs()}


@router.post("/generate")
def create_logs(count: int = Query(default=10, ge=1, le=100)):
    generated = generate_logs(count)
    return {
        "message": f"{count} logs generated successfully",
        "logs": generated,
    }