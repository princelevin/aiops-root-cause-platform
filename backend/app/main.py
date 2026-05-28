from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.services import router as services_router
from app.api.incidents import router as incidents_router
from app.api.simulation import router as simulation_router
from app.api.logs import router as logs_router

app = FastAPI(title="AIOps Root Cause Platform")

app.include_router(health_router)
app.include_router(services_router)
app.include_router(incidents_router)
app.include_router(simulation_router)
app.include_router(logs_router)