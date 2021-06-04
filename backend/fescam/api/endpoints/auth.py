from fastapi import APIRouter, Header, Depends
from fescam.schemas.funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.api.bearer import JWTBearer
from fescam.util.jwt import decode_jwt, encode_jwt
from typing import Any, Optional
import logging
import bcrypt
import re

router = APIRouter()
func_dao = FuncionarioDAO()

@router.get('/test')
async def teste():
    return {'msg': 'Olá Mundo'}

@router.post('/auth')
async def post_auth(func: Funcionario = None):
    if not func:
        return {'msg': 'Requisição vazia.'}

    cpf = re.sub(r'\D', '', func.CPF)
    funcionario = func_dao.findByPK(cpf)
    cpf_existe = bool(funcionario)
    encoded_senha = func.senha.encode('utf-8')
    logging.debug(f'funcionário senha: {funcionario.senha}')
    logging.debug(f'funcionário senha type: {type(funcionario.senha)}')

    if cpf_existe and bcrypt.checkpw(funcionario.senha, encoded_senha):
        return {'access_token': encode_jwt(cpf)}

    return {'msg': f'Esse funcionário não existe ou a senha está incorreta, CPF: "{cpf}".'}


@router.get('/auth', dependencies=[Depends(JWTBearer())])
async def ping():
    # Authentication: 'Bearer 423494293rirtrouier4992439432'
    return True