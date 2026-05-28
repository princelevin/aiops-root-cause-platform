from fastapi import APIRouter
from app.services.anomaly_detector import detect_anomalies

router = APIRouter(prefix="/api/anomalies", tags=["Anomalies"])


@router.post("/detect")
def run_anomaly_detection():
    anomalies = detect_anomalies()

    return {
        "message": f"{len(anomalies)} anomalies detected",
        "anomalies": anomalies,
    }