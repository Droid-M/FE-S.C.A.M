from fastapi import Request, HTTPException
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from fescam.util.jwt_use import decode_jwt
from fescam.DAO import FuncionarioDAO
from fescam.components.functions_helpers import ADMINISTRADOR_FOO

class Check(HTTPBearer):
    def __init__(self, allowedTypes:list, auto_error: bool = True):
        super(Check, self).__init__(auto_error=auto_error)
        self.types = allowedTypes

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(Check, self).__call__(request)
        payload = decode_jwt(credentials.credentials)
        result = FuncionarioDAO().findByPK(payload.get('cpf'))
        if(result is None or result.tipo not in self.types):
            raise HTTPException(status_code=422, detail="Unauthorized user.")