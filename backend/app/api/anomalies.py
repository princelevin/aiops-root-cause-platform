from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.anomaly_detector import detect_anomalies

router = APIRouter(prefix="/api/anomalies", tags=["Anomalies"])


@router.post("/detect")
def run_anomaly_detection(db: Session = Depends(get_db)):
    anomalies = detect_anomalies(db)

    return {
        "message": f"{len(anomalies)} anomalies detected",
        "anomalies": anomalies,
    }