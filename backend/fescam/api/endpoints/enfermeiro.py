from typing import Any, List, NoReturn
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from fescam.api.bearer import JWTBearer
from fescam.controller.EnfermeiroController import *

from fescam.components.functions_helpers import ENFERMEIRO_CHEFE_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_FOO, ESTAGIARIO_FOO
from fescam import schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

@router.get(
    '/enfermeiro', 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.EnfermeiroBase]
    )
async def getAllData(page: int = 0, per_page: int = -1):
    return read_all_enfermeiro(page, per_page)

@router.get('/enfermeiro/{enfermeiro_id}',dependencies=[Depends(JWTBearer())], response_model=schemas.EnfermeiroBase) #Response_model é realmente necessário?
async def getData(enfermeiro_id: str):
    return read_enfermeiro(enfermeiro_id)