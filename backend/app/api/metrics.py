from fastapi import APIRouter, Query

from app.services.metrics_generator import (
    generate_metrics,
    get_metrics,
    get_latest_service_metrics,
    get_metric_scenarios,
)


# APIs for generating and viewing service metrics
router = APIRouter(prefix="/api/metrics", tags=["Metrics"])


@router.get("")
def list_metrics():
    """
    Get latest generated metrics.
    """

    return {
        "metrics": get_metrics()
    }


@router.get("/latest")
def latest_metrics():
    """
    Get latest metric for each service.
    """

    return {
        "metrics": get_latest_service_metrics()
    }


@router.get("/scenarios")
def list_metric_scenarios():
    """
    Show available metric simulation scenarios.
    """

    return {
        "scenarios": get_metric_scenarios()
    }


@router.post("/generate")
def create_metrics(
    count: int = Query(default=10, ge=1, le=100),
    scenario: str = Query(default="normal"),
):
    """
    Generate fake metrics for a selected scenario.
    """

    # Generate metrics like normal traffic, CPU spike, memory leak, etc.
    generated = generate_metrics(count, scenario)

    return {
        "message": f"{count} {scenario} metrics generated successfully",
        "metrics": generated,
    }