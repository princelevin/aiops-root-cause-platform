from pydantic import BaseModel
from datetime import datetime


class Incident(BaseModel):
    id: int
    service: str
    title: str
    severity: str
    status: str
    root_cause_hint: str
    created_at: datetime