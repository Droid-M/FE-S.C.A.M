
from fescam import DAO, model, schemas
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Any, List, NoReturn
from fescam.controller.AdministradorController import *

router = APIRouter()

@router.get('/administrador', response_model=List[schemas.AdministradorBase])
async def getAllData(
    page: int = 0, 
    per_page: int = -1,
):
    return read_all_administrador(page, per_page)

# Response_model é realmente necessário?
@router.get('/administrador/{administrador_id}', response_model=schemas.AdministradorBase)
async def getData(administrador_id: str):
    return read_administrador(administrador_id)
