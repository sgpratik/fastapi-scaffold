from fastapi import APIRouter
from .api import server_status_check

health_router = APIRouter()

health_router.get("/check")(server_status_check)
