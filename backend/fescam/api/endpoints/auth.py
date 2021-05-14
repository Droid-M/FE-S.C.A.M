from fastapi import FastAPI, Header, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fescam.schemas.funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from typing import Optional
import bcrypt
import jwt
import re

router = FastAPI(prefix='/api')
func_dao = FuncionarioDAO()

SECRET = '123124'


@router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@router.post('/auth')
async def post_auth(func: Funcionario = None):
    if not func:
        return {'msg': 'Requisição vazia.'}
    cpf = re.sub(r'\D', '', func.CPF)
    funcionario = func_dao.findByPK(cpf)
    cpf_existe = bool(funcionario)
    encoded_senha = func.senha.encode('utf-8')

    if cpf_existe and bcrypt.checkpw(encoded_senha, funcionario.senha):
        payload = {'cpf':cpf}

        token = jwt.encode(
            payload,
            SECRET,
            algorithm='HS256'
        )
        return {'access_token': token}
    return {'msg': f'Esse funcionário não existe, CPF: "{cpf}".'}


@router.get('/auth')
async def ping(authentication: Optional[str] = Header(None)):
    encoded = authentication.replace('Bearer ', '')
    decoded = jwt.decode(encoded, SECRET, algorithms="HS256")
    cpf = decoded.get('cpf')
    if cpf and func_dao.findByPK(cpf):
        return True
    return False