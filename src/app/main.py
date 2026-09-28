from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.db.mongodb import lifespan


app = FastAPI(
    title="Customer Risk & Loan Platform",
    description="Advanced FastAPI learning project",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(
    health_router,
    prefix="/api/v1",
)