"""
FastAPI entry point for the AIOps Root Cause Analysis Platform.

This is where the backend app is created, database tables are initialized,
CORS is configured, and all feature routers are connected.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.models import database_models

from app.api.health import router as health_router
from app.api.services import router as services_router
from app.api.incidents import router as incidents_router
from app.api.simulation import router as simulation_router
from app.api.logs import router as logs_router
from app.api.failures import router as failures_router
from app.api.metrics import router as metrics_router
from app.api.anomalies import router as anomalies_router
from app.api.rca import router as rca_router
from app.api.correlation import router as correlation_router
from app.api.ai import router as ai_router
from app.api.ai_rca import router as ai_rca_router
from app.api.events import router as events_router
from app.api.reports import router as reports_router
from app.api.guardrails import router as guardrails_router


# Create the FastAPI app.
# This is the main backend application that runs on port 8000.
app = FastAPI(title="AIOps Root Cause Platform")


# Create database tables from the SQLAlchemy models.
# For this portfolio project, this keeps setup simple because tables are created
# automatically when the backend starts.
Base.metadata.create_all(bind=engine)


# Allow the React frontend to call this backend from the browser.
# The frontend runs on Vite at localhost:5173, so we whitelist that origin here.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Basic health check route.
# Useful to quickly confirm that the backend is running.
app.include_router(health_router)


# Simulated services used by the platform.
# These represent services like payment-service, order-service, and inventory-service.
app.include_router(services_router)


# Incident APIs.
# These expose the incidents created from failures and anomaly detection.
app.include_router(incidents_router)


# Simulation APIs.
# Used to simulate distributed service behavior for the demo.
app.include_router(simulation_router)


# Log APIs.
# Used to generate structured logs for incident and RCA workflows.
app.include_router(logs_router)


# Failure injection APIs.
# These manually trigger failures like Redis timeout or payment gateway failure.
app.include_router(failures_router)


# Metrics APIs.
# These generate service metrics such as latency, error rate, CPU, and memory usage.
app.include_router(metrics_router)


# Anomaly detection APIs.
# These scan metrics and create incidents when thresholds are crossed.
app.include_router(anomalies_router)


# Rule-based RCA APIs.
# This gives deterministic root cause analysis without using the LLM.
app.include_router(rca_router)


# Correlation APIs.
# Used to find related incidents based on service, failure type, severity, and cause.
app.include_router(correlation_router)


# Generic AI analysis APIs.
# Used to send simple prompts/context to the local Ollama model.
app.include_router(ai_router)


# AI-powered RCA APIs.
# These use Ollama/Llama to generate a more detailed root cause analysis.
app.include_router(ai_rca_router)


# Event queue APIs.
# These simulate async event processing for incident workflows.
app.include_router(events_router)


# Report APIs.
# Used to generate a complete incident report with RCA and timeline details.
app.include_router(reports_router)


# Guardrail APIs.
# These check whether the AI RCA output is grounded in the actual incident context.
app.include_router(guardrails_router)