from os import path
import sys

sys.path.append(path.abspath('.'))

from typing import Any, List, NoReturn

from fastapi import APIRouter, Depends, HTTPException, Response, responses, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from backend.app.components.functions_helpers import ENFERMEIRO_CHEFE_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_FOO, ESTAGIARIO_FOO
from backend.app import DAO, model, schemas

router = APIRouter()

admDAO = DAO.AdministradorDAO()
funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()

@router.get('/enfermeiro', response_model=List[schemas.EnfermeiroBase])
def read_all_enfermeiro(
        page: int = 0, per_page: int = -1,
        current_user: schemas.EnfermeiroBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            users = Depends(enfDAO.getAll())
            return Response(
                status_code= status.HTTP_200_OK, 
                description = 'Retorna uma lista de todos os usuários do sistema', 
                content = users
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get('/enfermeiro/{enfermeiro_id}', response_model=schemas.EnfermeiroBase) #Response_model é realmente necessário?
def read_enfermeiro(enfermeiro_id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        user = Depends(enfDAO.findByPK(enfermeiro_id))
        if(user is not None):
            nome = user.nome
            CPF = user.CPF
            created_on = user.created_on
            updated_on = user.updated_on
            user = schemas.EnfermeiroBase(
                nome = nome,
                CPF = CPF,
                created_on = created_on,
                updated_on = updated_on
                )
            return Response(
                status_code= status.HTTP_200_OK, 
                description = 'Retorna uma lista de todos os usuários do sistema', 
                content = user
                )
        return Response(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            description = f"ID/CPF de usuário {enfermeiro_id} não consta no sistema!",
            content= schemas.Error(message = f"ID/CPF de usuário {enfermeiro_id} não consta no sistema!")
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")