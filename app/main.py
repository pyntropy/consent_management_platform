from fastapi import FastAPI
from app.routers import consents_router

app = FastAPI(
    title="CMP",
    version="0.0.1"
)

app.include_router(consents_router)

