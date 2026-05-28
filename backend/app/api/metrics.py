from fastapi import APIRouter, Query
from app.services.metrics_generator import (
    generate_metrics,
    get_metrics,
    get_latest_service_metrics,
    get_metric_scenarios,
)

router = APIRouter(prefix="/api/metrics", tags=["Metrics"])


@router.get("")
def list_metrics():
    return {"metrics": get_metrics()}


@router.get("/latest")
def latest_metrics():
    return {"metrics": get_latest_service_metrics()}


@router.get("/scenarios")
def list_metric_scenarios():
    return {"scenarios": get_metric_scenarios()}


@router.post("/generate")
def create_metrics(
    count: int = Query(default=10, ge=1, le=100),
    scenario: str = Query(default="normal"),
):
    generated = generate_metrics(count, scenario)
    return {
        "message": f"{count} {scenario} metrics generated successfully",
        "metrics": generated,
    }