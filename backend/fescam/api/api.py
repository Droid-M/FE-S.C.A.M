from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import Header, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fescam.api.endpoints.auth import router as auth
from fescam.api.endpoints.administrador import router as administrador
from fescam.api.endpoints.enfermeiro import router as enfermeiro
from fescam.api.endpoints.enfermeiroChefe import router as enfermeiroChefe
from fescam.api.endpoints.estagiario import router as estagiario

from fastapi.staticfiles import StaticFiles

api_router = FastAPI()

@api_router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


#api_router.include_router(usersControl, tags=["user_control"])
api_router.include_router(auth, tags=["api_auth"])
api_router.include_router(administrador, tags=["administrador"])
api_router.include_router(enfermeiro, tags=["enfermeiro"])
api_router.include_router(enfermeiroChefe, tags=["enfermeiroChefe"])
api_router.include_router(estagiario, tags=["estagiario"])

api_router.mount("/static", StaticFiles(directory="../frontend/static"), name="static")