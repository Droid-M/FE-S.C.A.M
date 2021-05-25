from os import path
import sys

sys.path.append(path.abspath('.'))

from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from fescam.components.functions_helpers import ENFERMEIRO_CHEFE_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_FOO, ESTAGIARIO_FOO
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

admDAO = DAO.AdministradorDAO()
funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()

@router.get('/enfermeirochefe', dependencies=[Depends(JWTBearer())], response_model=List[schemas.EnfermeiroChefeBase])
def read_all_enfermeiro(
        page: int = 0, per_page: int = -1,
        current_user: schemas.EnfermeiroChefeBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            users = enfCFDAO.getAll()
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(users)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get('/enfermeirochefe/{enfermeiro_chefe_id}', dependencies=[Depends(JWTBearer())], response_model=schemas.EnfermeiroChefeBase) #Response_model é realmente necessário?
def read_enfermeiro(enfermeiro_chefe_id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        user = enfCFDAO.findByPK(enfermeiro_chefe_id)
        if(user is not None):
            nome = user.nome
            CPF = user.CPF
            created_on = user.created_on
            updated_on = user.updated_on
            user = schemas.EnfermeiroChefeBase(
                nome = nome,
                CPF = CPF,
                created_on = created_on,
                updated_on = updated_on
                )
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(user)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            #description = f"ID/CPF de usuário {enfermeiro_chefe_id} não consta no sistema!",
            content= jsonable_encoder(schemas.Error(message = f"ID/CPF de usuário {enfermeiro_chefe_id} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")