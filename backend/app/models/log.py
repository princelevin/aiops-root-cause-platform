from pydantic import BaseModel
from datetime import datetime


class LogEntry(BaseModel):
    # API schema for one generated log entry
    id: int
    service: str
    level: str
    message: str
    latency_ms: int
    timestamp: datetime