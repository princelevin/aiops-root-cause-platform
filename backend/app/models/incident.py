from pydantic import BaseModel
from datetime import datetime


class Incident(BaseModel):
    # API schema for returning incident details
    id: int
    service: str
    title: str
    severity: str
    status: str
    root_cause_hint: str
    created_at: datetime