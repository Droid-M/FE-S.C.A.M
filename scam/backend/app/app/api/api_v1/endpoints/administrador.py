from os import stat
from typing import Any, List, NoReturn

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from app import DAO, model, schemas
from app.api import deps

router = APIRouter()

funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()
admDAO = DAO.AdministradorDAO() 

@router.get("/lista_users", response_model=List[schemas.FuncionarioBase])
def getAllUsers(
        page: int = 0, per_page: int = -1,
        current_user: model.Administrador = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
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


@router.post("/cadastro_user", response_model=schemas.funcionario)
def create_user(
    user: schemas.FuncionarioCreated,
    user_type: str,
    current_user: model.Administrador = None
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = None
        if(user_type == "ADMINISTRADOR"):
            result = Depends(funcDAO.createBySchema(user))
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
                    content = users
                    )


@router.put("/{id}", response_model=schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.ItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
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
    """
    Get item by ID.
    """
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
    """
    Delete an item.
    """
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.item.remove(db=db, id=id)
    return item
