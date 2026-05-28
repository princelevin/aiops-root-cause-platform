from pydantic import BaseModel
from datetime import datetime


class MetricEntry(BaseModel):
    id: int
    service: str
    latency_ms: int
    error_rate: float
    request_count: int
    cpu_usage: float
    memory_usage: float
    timestamp: datetime