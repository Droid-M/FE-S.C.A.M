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
from fescam.api.endpoints.medicamento import router as medicamento
from fescam.api.endpoints.paciente import router as paciente
from fescam.api.endpoints.posologia import router as posologia
from fescam.api.endpoints.agendamento import router as agendamento
from fescam.db.seed.seed_db import prepare_DB
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="../frontend/templates")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
)


app.include_router(users, tags=["user_control"])
app.include_router(auth, tags=["api_auth"])
app.include_router(administrador, tags=["administrador"])
app.include_router(enfermeiro, tags=["enfermeiro"])
app.include_router(enfermeiroChefe, tags=["enfermeiroChefe"])
app.include_router(estagiario, tags=["estagiario"])
app.include_router(medicamento, tags=["medicamentos"])
app.include_router(paciente, tags=["pacientes"])
app.include_router(posologia, tags=["posologias"])
app.include_router(agendamento, tags=["agendamentos"])

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

#testando semeação de banco (e geração de arquivos) (tô ligado que testes de rota não feitos aqui kk)**********************
from fescam.db.generate_backup import backup
import os

@app.get("/teste_seed")
async def test_seed():
    prepare_DB()
    return {"message":"Dados completos. Cheque a pasta 'backend/fescam/db/scripts/seed_result' para obter as credenciais"}
#testando semeação de banco (e geração de arquivos) **********************


#testando dump sql (na segunda vez vai dar erro pq não permite sobrescrita de arquivo --proposital--): ***************
from fescam.db.generate_backup import backup
import os

@app.get("/teste_backup")
async def test():
    path = os.path.dirname(os.path.abspath(__file__)) + "/db/scripts/teste.sql"
    #path = os.path.dirname(os.path.abspath(__file__)) + "\\db\\scripts\\teste.sql" <-- Windows
    if(backup(path)):
        return f"Arquivo criado com sucesso! Localização: {path}"
    else:
        return f"Erro ao criar arquivo! Verifique as credenciais do banco ou se já existe algum arquivo no diretório {path}"
#testando dump sql ***************

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("login2.html",  {"request": request})

@app.get("/admin", response_class=HTMLResponse)
async def adm(request: Request):
    return templates.TemplateResponse("adm.html", {"request": request})

@app.get("/alarme", response_class=HTMLResponse)
async def alarme(request: Request):
    return templates.TemplateResponse("alarme.html",  {"request": request})

@app.get("/cadastrar-farmaco", response_class=HTMLResponse)
async def cadastrarFarmaco(request: Request):
    return templates.TemplateResponse("cadastrarFarmaco.html",  {"request": request})

@app.get("/cadastrar-paciente", response_class=HTMLResponse)
async def cadastrarPaciente(request: Request):
    return templates.TemplateResponse("cadastrarPaciente.html",  {"request": request})

@app.get("/cadastro-paciente", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastroPaciente.html",  {"request": request})

@app.get("/cadastro-usuario", response_class=HTMLResponse)
async def cadastroUsuario(request: Request):
    return templates.TemplateResponse("cadastroUsuario.html",  {"request": request})

@app.get("/designar-enfermeiro", response_class=HTMLResponse)
async def designarEnfermeiro(request: Request):
    return templates.TemplateResponse("designarEnfermeiro.html",  {"request": request})

@app.get("/enf", response_class=HTMLResponse)
async def enfermeiro(request: Request):
    return templates.TemplateResponse("enf.html",  {"request": request})

@app.get("/enf-chefe", response_class=HTMLResponse)
async def enfermeiroChefe(request: Request):
    return templates.TemplateResponse("enfchefe.html",  {"request": request})

@app.get("/fazer-backup", response_class=HTMLResponse)
async def fazerBackup(request: Request):
    return templates.TemplateResponse("fazerBackup.html",  {"request": request})

@app.get("/gerar-log", response_class=HTMLResponse)
async def gerarLog(request: Request):
    return templates.TemplateResponse("gerarLog.html",  {"request": request})

@app.get("/gerar-relatorio", response_class=HTMLResponse)
async def gerarRelatorio(request: Request):
    return templates.TemplateResponse("gerarRelatorio.html",  {"request": request})

@app.get("/listar-enfermeiro", response_class=HTMLResponse)
async def listaEnfermeiro(request: Request):
    return templates.TemplateResponse("listarEnfermeiros.html",  {"request": request})

@app.get("/listar-paciente", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("listarPaciente.html",  {"request": request})

@app.get("/navbar", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("navbar.html",  {"request": request})
    
@app.get("/sidebaradm", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("sidebarAdm.html",  {"request": request})

@app.get("/sidebarenfchefe", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("sidebarEnfChefe.html",  {"request": request})

@app.get("/sidebarenf", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("sidebarEnf.html",  {"request": request})