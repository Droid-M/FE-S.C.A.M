from fastapi import APIRouter, Depends, Response
from fescam.schemas.funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.api.bearer import JWTBearer
from fescam.util.jwt_use import decode_jwt, encode_jwt
import bcrypt
import re

router = APIRouter()
func_dao = FuncionarioDAO()

@router.post('/auth')
async def post_auth(response: Response, func: Funcionario = None):
    if not func:
        return {'msg': 'Requisição vazia.'}

    cpf = re.sub(r'\D', '', func.CPF) # Meu funcionario
    funcionario = func_dao.findByPK(cpf)  # Funcionario do bd 
    if(bool(funcionario)): 
        encoded_senha = func.senha.encode('utf-8')
        hashed = funcionario.senha.encode('utf-8')
        if bcrypt.checkpw(encoded_senha, hashed):
            remember_token = bool(func.remember_me)
            return {'access_token': encode_jwt(cpf, remember_token), 'classe': str(funcionario.tipo)}
    response.status_code = 406
    return {'msg': f'Esse funcionário não existe ou a senha está incorreta, CPF: "{cpf}".'}
    
@router.get('/auth', dependencies=[Depends(JWTBearer())])
async def ping():
    return True