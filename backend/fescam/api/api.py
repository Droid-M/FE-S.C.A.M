from fastapi import Request, status
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from fescam.api.endpoints.auth import router as auth
from fescam.api.endpoints.administrador import router as administrador
from fescam.api.endpoints.enfermeiro import router as enfermeiro
from fescam.api.endpoints.enfermeiroChefe import router as enfermeiroChefe
from fescam.api.endpoints.estagiario import router as estagiario
from fescam.api.endpoints.usersControl import router as users

from fastapi.staticfiles import StaticFiles

api_router = FastAPI()
templates = Jinja2Templates(directory="../frontend/templates")

@api_router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


api_router.include_router(users, tags=["user_control"])
api_router.include_router(auth, tags=["api_auth"])
api_router.include_router(administrador, tags=["administrador"])
api_router.include_router(enfermeiro, tags=["enfermeiro"])
api_router.include_router(enfermeiroChefe, tags=["enfermeiroChefe"])
api_router.include_router(estagiario, tags=["estagiario"])

api_router.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

@api_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login.html",  {"request": request})

@api_router.get("/admin", response_class=HTMLResponse)
async def adm(request: Request):
    return templates.TemplateResponse("adm.html", {"request": request})

@api_router.get("/alarme", response_class=HTMLResponse)
async def alarme(request: Request):
    return templates.TemplateResponse("alarme.html",  {"request": request})

@api_router.get("/cadastrar-farmaco", response_class=HTMLResponse)
async def cadastrarFarmaco(request: Request):
    return templates.TemplateResponse("cadastrarFarmaco.html",  {"request": request})

@api_router.get("/cadastrar-paciente", response_class=HTMLResponse)
async def cadastrarPaciente(request: Request):
    return templates.TemplateResponse("cadastrarPaciente.html",  {"request": request})

@api_router.get("/cadastro-paciente", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastroPaciente.html",  {"request": request})

@api_router.get("/cadastro-usuario", response_class=HTMLResponse)
async def cadastroUsuario(request: Request):
    return templates.TemplateResponse("cadastroUsuario.html",  {"request": request})

@api_router.get("/designar-enfermeiro", response_class=HTMLResponse)
async def designarEnfermeiro(request: Request):
    return templates.TemplateResponse("designarEnfermeiro.html",  {"request": request})

@api_router.get("/enf", response_class=HTMLResponse)
async def enfermeiro(request: Request):
    return templates.TemplateResponse("enf.html",  {"request": request})

@api_router.get("/enf-chefe", response_class=HTMLResponse)
async def enfermeiroChefe(request: Request):
    return templates.TemplateResponse("enfchefe.html",  {"request": request})

@api_router.get("/fazer-backup", response_class=HTMLResponse)
async def fazerBackup(request: Request):
    return templates.TemplateResponse("fazerBackup.html",  {"request": request})

@api_router.get("/gerar-log", response_class=HTMLResponse)
async def gerarLog(request: Request):
    return templates.TemplateResponse("gerarLog.html",  {"request": request})

@api_router.get("/gerar-relatorio", response_class=HTMLResponse)
async def gerarRelatorio(request: Request):
    return templates.TemplateResponse("gerarRelatorio.html",  {"request": request})

@api_router.get("/listar-enfermeiro", response_class=HTMLResponse)
async def listaEnfermeiro(request: Request):
    return templates.TemplateResponse("listarEnfermeiros.html",  {"request": request})

@api_router.get("/listar-paciente", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("listarPaciente.html",  {"request": request})


    
