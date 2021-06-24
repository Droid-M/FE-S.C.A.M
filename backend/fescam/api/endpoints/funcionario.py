from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from fescam import DAO, model, schemas

from fescam.controller.FuncionarioController import *

router = APIRouter()

admDAO = DAO.AdministradorDAO()
funcDAO = DAO.FuncionarioDAO()
estDAO = DAO.EstagiarioDAO()
enfDAO = DAO.EnfermeiroDAO()
enfCFDAO = DAO.EnfermeiroChefeDAO()

@router.get(
    "/lista_usuario", 
    
    response_model=List[schemas.FuncionarioCreated]
    ) 
async def getAllData(page: int = 0, per_page: int = -1):
    return getAllUsers(page, per_page)

@router.get("/lista_usuario/{user_id}", response_model=schemas.FuncionarioBase) #Response_model é realmente necessário?
async def getData(user_id: str):
    return getUser(user_id)

@router.post(
    "/cadastro_usuario", 
    
    response_model=schemas.FuncionarioBase
    )
async def postData(user: schemas.FuncionarioCreated):
    return create_user(user)

@router.put("/edicao_usuario/{user_id}")
async def updateData(
    user: schemas.FuncionarioCreated,
    user_id: str
):
    return update_user(user, user_id)

@router.delete("/edicao_usuario/{user_id}")
async def deleteData(user_id: str):
    return delete_user(user_id)