from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.anomaly_detector import detect_anomalies


# APIs for detecting abnormal metrics and creating incidents
router = APIRouter(prefix="/api/anomalies", tags=["Anomalies"])


@router.post("/detect")
def run_anomaly_detection(db: Session = Depends(get_db)):
    """
    Detect anomalies from generated service metrics.
    """

    # Run anomaly detection logic from service layer
    anomalies = detect_anomalies(db)

    # Return anomaly count and details
    return {
        "message": f"{len(anomalies)} anomalies detected",
        "anomalies": anomalies,
    }