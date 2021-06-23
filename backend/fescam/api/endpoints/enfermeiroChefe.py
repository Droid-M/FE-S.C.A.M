from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from fescam.controller.EnfermeiroChefeController import *
from fescam.components.functions_helpers import ENFERMEIRO_CHEFE_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_FOO, ESTAGIARIO_FOO
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

@router.get('/enfermeirochefe', dependencies=[Depends(JWTBearer())], response_model=List[schemas.EnfermeiroChefeBase])
async def getAllData(page: int = 0, per_page: int = -1):
    return read_all_enfermeiro(page, per_page)

@router.get('/enfermeirochefe/{enfermeiro_chefe_id}', dependencies=[Depends(JWTBearer())], response_model=schemas.EnfermeiroChefeBase) #Response_model é realmente necessário?
async def getData(enfermeiro_chefe_id: str):
    return read_enfermeiro(enfermeiro_chefe_id)