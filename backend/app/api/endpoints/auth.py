from fastapi import APIRouter
from backend.app.schemas.funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
import bcrypt
import jwt
import re

router = APIRouter()


@router.post('/')
async def post_auth(func: Funcionario):
    cpf = re.sub(r'\D', '', func.CPF)
    funcionario = FuncionarioDAO.findByPK(cpf)
    cpf_existe = bool(funcionario)
    encoded_senha = func.senha.encode('utf-8')

    if cpf_existe and bcrypt.checkpw(encoded_senha, funcionario.senha):
        payload = {'cpf':cpf}

        token = jwt.encode(
            payload,
            'SECRET_KEY',
            algorithm='HS256'
        )
        return {'access_token': token}
    return {'msg': f'Esse funcionário não existe, CPF: {cpf}.'}