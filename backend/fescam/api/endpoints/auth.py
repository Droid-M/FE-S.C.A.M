from fastapi import APIRouter, Header
from fescam.schemas.funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from typing import Optional
import bcrypt
import jwt
import re

router = APIRouter(prefix='/api')
func_dao = FuncionarioDAO()

SECRET = '123124'


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