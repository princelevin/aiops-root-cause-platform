# System Design

## High-Level Design

The AIOps Root Cause Analysis Platform follows a layered architecture pattern.

```text
Presentation Layer
        │
        ▼
Application Layer
        │
        ▼
Domain Services Layer
        │
        ▼
Persistence Layer
        │
        ▼
AI Intelligence Layer
```

---

# Request Flow

## Failure Injection Workflow

```text
Failure Injected
      │
      ▼
Incident Created
      │
      ▼
Severity Assigned
      │
      ▼
Event Published
      │
      ▼
RCA Generated
      │
      ▼
Guardrail Validation
      │
      ▼
Report Generated
```

---

# Frontend Layer

## Responsibilities

- Dashboard visualization
- Incident management
- RCA visualization
- Report viewing
- Timeline inspection

## Technologies

- React
- Vite
- CSS

---

# API Layer

## Responsibilities

- Request validation
- Routing
- Response formatting
- Business workflow orchestration

## Technologies

- FastAPI
- Pydantic

---

# Service Layer

The service layer contains the core business logic.

## Incident Service

Handles:

- Incident creation
- Status updates
- Lifecycle tracking

## RCA Service

Handles:

- Root cause generation
- Recommendation generation
- Confidence scoring

## Severity Service

Handles:

- Priority assignment
- Impact evaluation

## Guardrail Service

Handles:

- AI output validation
- Context verification

## Report Service

Handles:

- Executive reporting
- Timeline aggregation

---

# Event Processing Layer

The platform implements an internal event queue.

Current event lifecycle:

```text
INCIDENT_CREATED
       │
       ▼
FAILURE_DETECTED
       │
       ▼
RCA_GENERATED
       │
       ▼
INCIDENT_RESOLVED
```

Future migration path:

```text
Internal Queue
      │
      ▼
Apache Kafka
      │
      ▼
Distributed Event Streaming
```

---

# Database Design

## Incident Table

Stores:

- Service
- Severity
- Status
- Root Cause Hint
- Failure Type
- Latency

---

## RCA Table

Stores:

- Root Cause
- Recommendation
- Confidence Score

---

## Timeline Table

Stores:

- Incident history
- Workflow events
- Audit trail

---

## Event Queue Table

Stores:

- Pending events
- Processed events
- Event metadata

---

# AI Layer Design

## Local LLM Architecture

```text
Incident Context
        │
        ▼
Prompt Builder
        │
        ▼
Ollama (Llama 3.2)
        │
        ▼
RCA Output
        │
        ▼
Guardrail Validation
```

### Benefits

- No API cost
- Low latency
- Data privacy
- Offline execution

---

# Security Considerations

- Input validation
- Context grounding
- AI hallucination prevention
- Controlled recommendation generation
- Explainable AI outputs

---

# Testing Strategy

## Framework

- Pytest

## Current Coverage

- Severity Engine
- Guardrail Engine
- Health API

## Test Status

✅ All automated tests passing

---

# Scalability Strategy

## Current State

- Single-node deployment
- SQLite persistence
- Local AI inference

## Enterprise Upgrade Path

- PostgreSQL
- Apache Kafka
- Redis
- Docker
- Kubernetes
- Prometheus
- Grafana

---

# Production Readiness Roadmap

### Phase 1
- Local AIOps Platform
- AI RCA
- Guardrails
- Reporting

### Phase 2
- Dockerized Deployment
- PostgreSQL
- Redis

### Phase 3
- Kafka Event Streaming
- Kubernetes Deployment
- Observability Stack

### Phase 4
- Multi-LLM Support
- ServiceNow Integration
- Enterprise Incident Management

---

# Conclusion

The AIOps Root Cause Analysis Platform demonstrates a complete incident management lifecycle, combining event-driven architecture, AI-powered root cause analysis, guardrail validation, reporting, and automated testing into a production-inspired engineering solution.