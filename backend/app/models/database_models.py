from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base


class IncidentDB(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, index=True)
    title = Column(String)
    severity = Column(String)
    status = Column(String)
    root_cause_hint = Column(String)
    failure_type = Column(String)
    latency_ms = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


class LogDB(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, index=True)
    level = Column(String)
    message = Column(String)
    latency_ms = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)


class MetricDB(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, index=True)
    latency_ms = Column(Integer)
    error_rate = Column(Float)
    request_count = Column(Integer)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


class FailureDB(Base):
    __tablename__ = "failures"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String, index=True)
    level = Column(String)
    message = Column(String)
    latency_ms = Column(Integer)
    failure_type = Column(String)
    probable_cause = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)