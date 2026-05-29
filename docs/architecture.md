# AIOps Root Cause Analysis Platform

## Executive Summary

The AIOps Root Cause Analysis Platform is an AI-powered incident intelligence system designed to automate failure detection, incident management, root cause analysis, recommendation generation, and operational reporting.

The platform simulates real-world Site Reliability Engineering (SRE) and AIOps workflows commonly used in modern cloud-native environments.

### Key Capabilities

- Automated incident creation
- Dynamic severity classification
- Event-driven processing
- AI-powered root cause analysis
- Recommendation generation
- AI guardrails and validation
- Incident timeline tracking
- Executive reporting

---

# Business Problem

Modern engineering teams receive thousands of alerts daily.

Engineers often spend significant time answering:

- What failed?
- Why did it fail?
- Which service is impacted?
- What should be done next?

This platform automates that workflow.

Instead of manually investigating incidents, teams receive AI-assisted root cause analysis and actionable recommendations within seconds.

---

# Architecture Overview

```text
┌─────────────────────────────┐
│       React Dashboard       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│        FastAPI APIs         │
└─────────────┬───────────────┘
              │
 ┌────────────┼────────────┐
 ▼            ▼            ▼

Incident   RCA Engine   Event Engine
Engine     + AI         Processing

 ▼            ▼            ▼

 SQLite    Ollama     Event Queue

              ▼

       Guardrail Layer

              ▼

       Reporting Layer
```

---

# Core Components

## Incident Management Engine

Responsible for:

- Incident creation
- Status management
- Lifecycle tracking
- Metadata storage

Outputs:

- Open incidents
- Resolved incidents
- Historical records

---

## Severity Classification Engine

Assigns business impact levels.

| Severity | Meaning |
|-----------|----------|
| P0 | Critical outage |
| P1 | Major production issue |
| P2 | Performance degradation |
| P3 | Minor operational issue |

The engine combines:

- Failure type
- Service impact
- Latency thresholds

to determine incident priority.

---

## Event Processing Engine

Implements an event-driven architecture.

Supported events:

- INCIDENT_CREATED
- FAILURE_DETECTED
- RCA_GENERATED
- RECOMMENDATION_CREATED
- INCIDENT_RESOLVED

Benefits:

- Loose coupling
- Workflow orchestration
- Future Kafka compatibility

---

## Root Cause Analysis Engine

Analyzes incident context and operational signals.

### Inputs

- Failure metadata
- Service information
- Historical RCA data
- Incident severity

### Outputs

- Root cause hypothesis
- Confidence score
- Resolution recommendation

---

## AI Recommendation Layer

Powered by:

- Ollama
- Llama 3.2

Responsibilities:

- RCA generation
- Recommendation generation
- Incident summarization

The model operates locally without external API dependencies.

---

## AI Guardrail Engine

Prevents hallucinated recommendations.

Validates:

- Root cause consistency
- Context grounding
- Recommendation relevance

This ensures AI outputs remain explainable and trustworthy.

---

## Reporting Engine

Generates complete incident reports containing:

- Incident metadata
- RCA findings
- Timeline events
- Recommendations
- Confidence scores

Used by:

- Engineers
- SRE Teams
- Operations Teams
- Management

---

# Technology Stack

## Frontend

- React
- Vite
- CSS

## Backend

- FastAPI
- Python

## Database

- SQLite

## AI Layer

- Ollama
- Llama 3.2

## Testing

- Pytest

---

# Engineering Principles

The platform is designed around:

- Modular Architecture
- Event-Driven Processing
- Explainable AI
- Separation of Concerns
- Testability
- Extensibility

Every module can evolve independently without affecting the rest of the system.

---

# Future Enhancements

- PostgreSQL
- Apache Kafka
- Prometheus
- Grafana
- Kubernetes
- ServiceNow Integration
- Jira Integration
- Slack Alerting
- Multi-LLM Support

---

# Outcome

The platform demonstrates how AI can accelerate incident response workflows while maintaining reliability, explainability, and operational governance.