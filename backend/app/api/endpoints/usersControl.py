from os import path
import sys

sys.path.append(path.abspath('.'))

from typing import Any, List, NoReturn

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from backend.app import DAO, model, schemas
from backend.app.api import deps

router = APIRouter()

admDAO = DAO.AdministradorDAO()
funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()

@router.get("/lista_users", response_model=List[schemas.FuncionarioBase])
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


@router.post("/cadastro_user", response_model=schemas.FuncionarioBase)
def create_user(
    user: schemas.FuncionarioCreated,
    user_type: str,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = None
        if(user_type == "ADMINISTRADOR"):
            result = Depends(admDAO.createBySchema(user))
        elif(user_type == "ESTAGIARIO"):
            result = Depends(estDAO.createBySchema(user))
        elif(user_type == "ENFERMEIRO"):
            result = Depends(enfDAO.createBySchema(user))
        elif(user_type == "ENFERMEIRO_CHEFE"):
            result = Depends(enfCFDAO.createBySchema(user))
        
        if(result is not None):
            user = schemas.FuncionarioBase(**result.typesAceptables)
            return Response(
                status_code= status.HTTP_200_OK, 
                description = 'Um novo usuario foi cadastrado com sucesso', 
                content = user
                )
        else:
            return Response(
                status_code= status.HTTP_406_NOT_ACCEPTABLE,
                description = f"Tipo de usuário {user_type} não é permitido!",
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