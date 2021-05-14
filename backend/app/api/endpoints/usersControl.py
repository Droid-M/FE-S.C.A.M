from os import path
import sys

sys.path.append(path.abspath('.'))

from typing import Any, List, NoReturn

from fastapi import APIRouter, Depends, HTTPException, Response, responses, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from backend.app.components.functions_helpers import ENFERMEIRO_CHEFE_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_FOO, ESTAGIARIO_FOO
from backend.app import DAO, model, schemas
from backend.app.api import deps

router = APIRouter()

admDAO = DAO.AdministradorDAO()
funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()

@router.get("/lista_usuario", response_model=List[schemas.FuncionarioBase]) #Response_model é realmente necessário?
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
            users = Depends(funcDAO.getAll())
            return Response(
                status_code= status.HTTP_200_OK, 
                description = 'Retorna uma lista de todos os usuários do sistema', 
                content = users
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")


@router.post("/cadastro_usuario", response_model=schemas.FuncionarioBase)
def create_user(
    user: schemas.FuncionarioCreated,
    user_type: str,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = None
        if(user_type == ADMINISTRADOR_FOO):
            result = Depends(admDAO.createBySchema(user))
        elif(user_type == ESTAGIARIO_FOO):
            result = Depends(estDAO.createBySchema(user))
        elif(user_type == ENFERMEIRO_FOO):
            result = Depends(enfDAO.createBySchema(user))
        elif(user_type == ENFERMEIRO_CHEFE_FOO):
            result = Depends(enfCFDAO.createBySchema(user))
        
        if(result is not None):
            nome = result.nome
            CPF = result.CPF
            created_on = result.created_on
            updated_on = result.updated_on
            user = schemas.FuncionarioBase(nome = nome, CPF = CPF, created_on = created_on, updated_on = updated_on)
            return Response(
                status_code = status.HTTP_200_OK,
                description = 'Um novo usuario foi cadastrado com sucesso', 
                content = user
                )
        else:
            return Response(
                status_code = status.HTTP_406_NOT_ACCEPTABLE,
                description = f"Tipo de usuário {user_type} não é permitido!",
                content= schemas.Error(message = f"Tipo de usuário {user_type} não é permitido!")
            )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.put("/edicao_usuario/{user_id}") #<-- Ainda não suporta atualização de chave primária *******
def update_user(
    user: schemas.FuncionarioCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        user_updated = Depends(funcDAO.update(user))
        if(user_updated is not None):
            return Response(
                status_code = status.HTTP_200_OK,
                description = 'Atualização realizada com sucesso', 
                content = schemas.FuncionarioBase(
                    CPF = user_updated.CPF, 
                    nome = user_updated.nome, 
                    updated_on = user_updated.updated_on, 
                    created_on = user_updated.created_on
                ))
        return Response(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            description = f"Impossível atualizar um usuário não cadastrado! CPF:{user.CPF}",
            content= schemas.Error(message = f"Impossível atualizar um usuário não cadastrado! CPF:{user.CPF}")
            )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/edicao_usuario/{user_id}")
def delete_user(id):
    is_admin = True
    if(is_admin):
        deleted_user = Depends(funcDAO.DeleteByPK(id))
        if(deleted_user is not None):
            return Response(
                status_code = status.HTTP_200_OK,
                description = 'Usuario deletado com sucesso', 
                content = schemas.FuncionarioBase(
                    CPF = deleted_user.CPF, 
                    nome = deleted_user.nome, 
                    updated_on = deleted_user.updated_on, 
                    created_on = deleted_user.created_on
                ))
        return Response(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            description = f"Impossível remover um usuário não cadastrado! CPF:{id}",
            content= schemas.Error(message = f"Impossível remover um usuário não cadastrado! CPF:{id}")
            )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

"""
@router.put("/{id}", response_model=schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.ItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.Item)
def read_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.remove(db=db, id=id)
    return item
"""