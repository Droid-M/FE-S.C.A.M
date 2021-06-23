from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from starlette.status import HTTP_404_NOT_FOUND
from fescam.controller.EstagiarioController import *
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

@router.get('/estagiario', dependencies=[Depends(JWTBearer())], response_model=List[schemas.EstagiarioBase])
async def getAllData(page: int = 0, per_page: int = -1):
    return read_all_estagiario(page, per_page)

@router.get('/estagiario/{estagiario_id}', dependencies=[Depends(JWTBearer())], response_model=schemas.EstagiarioBase) #Response_model é realmente necessário?
async def getData(estagiario_id: str):
    return read_enfermeiro(estagiario_id)