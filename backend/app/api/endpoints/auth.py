from fastapi import APIRouter, Header
from backend.app.schemas.funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
from typing import Optional
import bcrypt
import jwt
import re

router = APIRouter(prefix='/api')

SECRET = '123124'


@router.post('/auth')
async def post_auth(func: Funcionario):
    cpf = re.sub(r'\D', '', func.CPF)
    funcionario = FuncionarioDAO.findByPK(cpf)
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
    return {'msg': f'Esse funcionário não existe, CPF: {cpf}.'}


@router.get('/auth')
async def ping(authentication: Optional[str] = Header(None)):
    encoded = re.sub('Bearer ', '', authentication)
    decoded = jwt.decode(encoded, SECRET, algorithms="HS256")
    cpf = decoded.get('cpf')
    if cpf and FuncionarioDAO.findByPK(cpf):
        return True
    return False