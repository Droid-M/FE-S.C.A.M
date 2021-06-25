import bcrypt
import os
from fastapi import Request, status
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from fescam.api.bearer import JWTBearer
from fescam.api.endpoints.auth import router as auth
from fescam.api.endpoints.administrador import router as administrador
from fescam.api.endpoints.enfermeiro import router as enfermeiro
from fescam.api.endpoints.enfermeiroChefe import router as enfermeiroChefe
from fescam.api.endpoints.estagiario import router as estagiario
from fescam.api.endpoints.funcionario import router as users
from fescam.api.endpoints.medicamento import router as medicamento
from fescam.api.endpoints.paciente import router as paciente
from fescam.api.endpoints.posologia import router as posologia
from fescam.api.endpoints.agendamento import router as agendamento
from fescam.db.seed.seed_db import prepare_DB
from fastapi.staticfiles import StaticFiles
from fescam.components.functions_helpers import ENFERMEIRO_FOO, ESTAGIARIO_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_CHEFE_FOO
from fescam.util import checkAccess
from fescam import DAO

app = FastAPI()

adm_auth = checkAccess.Check([ADMINISTRADOR_FOO])

templates = Jinja2Templates(directory="../frontend/templates")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
)

app.include_router(users, tags=["user_control"], dependencies=[Depends(JWTBearer()), Depends(adm_auth)])
app.include_router(auth, tags=["api_auth"])
app.include_router(administrador, tags=["administrador"], dependencies=[Depends(JWTBearer()), Depends(adm_auth)])
app.include_router(enfermeiro, tags=["enfermeiro"], dependencies=[Depends(JWTBearer())])
app.include_router(enfermeiroChefe, tags=["enfermeiroChefe"], dependencies=[Depends(JWTBearer())])
app.include_router(estagiario, tags=["estagiario"], dependencies=[Depends(JWTBearer())])
app.include_router(medicamento, tags=["medicamentos"], dependencies=[Depends(JWTBearer())])
app.include_router(paciente, tags=["pacientes"], dependencies=[Depends(JWTBearer())])
app.include_router(posologia, tags=["posologias"], dependencies=[Depends(JWTBearer())])
app.include_router(agendamento, tags=["agendamentos"], dependencies=[Depends(JWTBearer())])

app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

#testando semeação de banco (e geração de arquivos) (tô ligado que testes de rota não feitos aqui kk)**********************
from fescam.db.generate_backup import backup
import os

@app.get("/init_user")
async def create_first():
    senha = bcrypt.hashpw("12345678".encode('utf-8'), bcrypt.gensalt()).decode()
    CPF = "00000000000"
    tipo = "ADMINISTRADOR"
    return JSONResponse(
        status_code=200,
        content = jsonable_encoder(DAO.FuncionarioDAO().createByTuple(CPF = CPF, senha = senha, tipo = tipo, nome = "Admin"))
    )
            
@app.get("/teste_seed")
async def test_seed():
    prepare_DB()
    return {"message":"Dados completos. Cheque a pasta 'backend/fescam/db/scripts/seed_result' para obter as credenciais"}
#testando semeação de banco (e geração de arquivos) **********************

@app.get("/teste_backup")
async def test():
    path = os.path.dirname(os.path.abspath(__file__)) + "/db/scripts/teste.sql"
    os.remove(path)
    if(backup(path)):
        return FileResponse(path)
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

@app.get("/cadastro-paciente", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastro.Paciente.EnfChefe.html",  {"request": request})

@app.get("/cadastro-paciente/id={id_paciente}", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastro.Paciente.EnfChefe.html",  {"request": request}) 

@app.get("/enf/cadastro-paciente", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastro.Paciente.Enf.html",  {"request": request})

@app.get("/enf/cadastro-paciente/id={id_paciente}", response_class=HTMLResponse)
async def cadastroPaciente(request: Request):
    return templates.TemplateResponse("cadastro.Paciente.Enf.html",  {"request": request})     

@app.get("/cadastro-usuario", response_class=HTMLResponse)
async def cadastroUsuario(request: Request):
    return templates.TemplateResponse("cadastroUsuario.html",  {"request": request})

@app.get("/edicao-usuario/id={id_user}", response_class=HTMLResponse)
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

@app.get("/enf/listar-paciente", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("lista.Paciente.Enf.html",  {"request": request})

@app.get("/enf-chefe/listar-paciente", response_class=HTMLResponse)
async def listaPaciente(request: Request):
    return templates.TemplateResponse("lista.Paciente.EnfChefe.html",  {"request": request})

    
