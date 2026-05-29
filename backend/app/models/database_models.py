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

class IncidentTimelineDB(Base):
    __tablename__ = "incident_timeline"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, index=True)
    event_type = Column(String)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class RootCauseAnalysisDB(Base):
    __tablename__ = "root_cause_analyses"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, index=True)
    service = Column(String, index=True)
    severity = Column(String)
    failure_type = Column(String)
    root_cause = Column(String)
    recommendation = Column(String)
    confidence_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)