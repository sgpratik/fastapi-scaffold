from fastapi import APIRouter
from app.api.health import health_router


ENDPOINTS = [health_router]

router = APIRouter()
for endpoint in ENDPOINTS:
    router.include_router(endpoint)

__all__ = ['router']
