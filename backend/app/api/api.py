from os import path
import sys

sys.path.append(path.abspath('.'))

from fastapi import APIRouter
from backend.app.api.endpoints import usersControl, auth, administrador, enfermeiro, enfermeiroChefe, estagiario

api_router = APIRouter()
api_router.include_router(usersControl.router, tags=["user_control"])
api_router.include_router(auth.router, tags=["api_auth"])
api_router.include_router(administrador.router, tags=["administrador"])
api_router.include_router(enfermeiro.router, tags=["enfermeiro"])
api_router.include_router(enfermeiroChefe.router, tags=["enfermeiroChefe"])
api_router.include_router(estagiario.router, tags=["estagiario"])

#api_router.include_router(login.router, tags=["login"])
#api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
#api_router.include_router(administrador.router, prefix="/administrador", tags=["administrador"])
