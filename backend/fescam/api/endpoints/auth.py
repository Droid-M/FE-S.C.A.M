from fastapi import APIRouter, Depends
from fescam.schemas.funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.api.bearer import JWTBearer
from fescam.util.jwt_use import decode_jwt, encode_jwt
import bcrypt
import re

router = APIRouter()
func_dao = FuncionarioDAO()

@router.post('/auth')
async def post_auth(func: Funcionario = None):
    if not func:
        return {'msg': 'Requisição vazia.'}

    cpf = re.sub(r'\D', '', func.CPF) # Meu funcionario
    funcionario = func_dao.findByPK(cpf)  # Funcionario do bd 
    cpf_existe = bool(funcionario)
    encoded_senha = func.senha.encode('utf-8')
    senha_bd = funcionario.senha
    hashed = bcrypt.hashpw(senha_bd.encode('utf8'),bcrypt.gensalt())

    # if bcrypt.checkpw(encoded_senha,hashed):
    #     return {'msg': "Problema de hash"}
    # return {'Error': "Error brabo"}
    if cpf_existe and bcrypt.checkpw(encoded_senha, hashed):
        # return {'classe': str(funcionario.tipo)}
        return {'access_token': encode_jwt(cpf), 'classe': str(funcionario.tipo)}

    return {'msg': f'Esse funcionário não existe ou a senha está incorreta, CPF: "{cpf}".'}


@router.get('/auth', dependencies=[Depends(JWTBearer())])
async def ping():
    # Authentication: 'Bearer 423494293rirtrouier4992439432'
    return True