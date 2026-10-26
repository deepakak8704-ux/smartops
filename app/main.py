from fastapi import FastAPI
from .logs.routes import router as log_router
from .database import engine, Base
from . import models
from .employees.routes import router as employee_router
from .monitoring.routes import router as monitoring_router
from .service_requests.routes import (
    router as service_request_router
)

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="SmartOps",
    description="Intelligent IT Operations & Service Management Platform",
    version="1.0.0"
)

app.include_router(log_router)
app.include_router(employee_router)
app.include_router(monitoring_router)
app.include_router(service_request_router)

@app.get("/")
def root():
    return {
        "message": "SmartOps is running successfully!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
