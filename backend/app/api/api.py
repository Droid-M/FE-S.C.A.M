from fastapi import APIRouter

from backend.app.api.endpoints import administrador, items, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(administrador.router, prefix="/administrador", tags=["administrador"])
