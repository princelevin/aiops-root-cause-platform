from pydantic import BaseModel
from datetime import datetime


class LogEntry(BaseModel):
    id: int
    service: str
    level: str
    message: str
    latency_ms: int
    timestamp: datetime