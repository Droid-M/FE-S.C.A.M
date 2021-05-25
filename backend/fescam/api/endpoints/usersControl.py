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

@router.get("/lista_usuario", dependencies=[Depends(JWTBearer())], response_model=List[schemas.FuncionarioBase]) #Response_model é realmente necessário?
def getAllUsers(
        page: int = 0, per_page: int = -1,
        current_user: schemas.FuncionarioBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            users = funcDAO.getAll(convert = False)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(users)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get("/lista_usuario/{user_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.FuncionarioBase) #Response_model é realmente necessário?
def getAllUsers(user_id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        user = funcDAO.findByPK(user_id)
        if(user is not None):
            nome = user.nome
            CPF = user.CPF
            created_on = user.created_on
            updated_on = user.updated_on
            user = schemas.FuncionarioBase(
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
            #description = f"ID/CPF de usuário {user_id} não consta no sistema!",
            content= jsonable_encoder(schemas.Error(message = f"ID/CPF de usuário {user_id} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.post("/cadastro_usuario", dependencies=[Depends(JWTBearer())], response_model=schemas.FuncionarioBase)
def create_user(
    user: schemas.FuncionarioCreated,
    user_type: str,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = None
        if(user_type == ADMINISTRADOR_FOO):
            result = admDAO.createBySchema(user)
        elif(user_type == ESTAGIARIO_FOO):
            result = estDAO.createBySchema(user)
        elif(user_type == ENFERMEIRO_FOO):
            result = enfDAO.createBySchema(user)
        elif(user_type == ENFERMEIRO_CHEFE_FOO):
            result = enfCFDAO.createBySchema(user)
        
        if(result is not None):
            nome = result.nome
            CPF = result.CPF
            created_on = result.created_on
            updated_on = result.updated_on
            user = schemas.FuncionarioBase(nome = nome, CPF = CPF, created_on = created_on, updated_on = updated_on)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(user)
                )
        else:
            return JSONResponse(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                #description = f"Tipo de usuário {user_type} não é permitido!",
                content= jsonable_encoder(schemas.Error(message = f"Tipo de usuário {user_type} não é permitido!"))
            )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.put("/edicao_usuario", dependencies=[Depends(JWTBearer())]) #<-- Ainda não suporta atualização de chave primária *******
def update_user(
    user: schemas.FuncionarioCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        user_updated = funcDAO.update(user)
        if(user_updated is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(schemas.FuncionarioBase(
                    CPF = user_updated.CPF, 
                    nome = user_updated.nome, 
                    updated_on = user_updated.updated_on, 
                    created_on = user_updated.created_on
                )))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            #description = f"Impossível atualizar um usuário não cadastrado! CPF:{user.CPF}",
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar um usuário não cadastrado! CPF:{user.CPF}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/edicao_usuario/{user_id}", dependencies=[Depends(JWTBearer())])
def delete_user(user_id: int):
    is_admin = True
    if(is_admin):
        deleted_user = funcDAO.DeleteByPK(user_id)
        if(deleted_user is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(schemas.FuncionarioBase(
                    CPF = deleted_user.CPF, 
                    nome = deleted_user.nome, 
                    updated_on = deleted_user.updated_on, 
                    created_on = deleted_user.created_on
                )))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            #description = f"Impossível remover um usuário não cadastrado! CPF:{id}",
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover um usuário não cadastrado! CPF:{user_id}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")