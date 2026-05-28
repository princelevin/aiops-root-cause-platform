from fastapi import APIRouter, Query
from app.services.metrics_generator import (
    generate_metrics,
    get_metrics,
    get_latest_service_metrics,
)

router = APIRouter(prefix="/api/metrics", tags=["Metrics"])


@router.get("")
def list_metrics():
    return {"metrics": get_metrics()}


@router.get("/latest")
def latest_metrics():
    return {"metrics": get_latest_service_metrics()}


@router.post("/generate")
def create_metrics(count: int = Query(default=10, ge=1, le=100)):
    generated = generate_metrics(count)
    return {
        "message": f"{count} metrics generated successfully",
        "metrics": generated,
    }