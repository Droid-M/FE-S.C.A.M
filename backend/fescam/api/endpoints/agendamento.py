import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam.controller.AgendamentoController import *
from fescam import DAO, model, schemas
from fescam.components.functions_helpers import ENFERMEIRO_FOO, ESTAGIARIO_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_CHEFE_FOO
from fescam.util import checkAccess

router = APIRouter()
enfCf = checkAccess.Check([ENFERMEIRO_CHEFE_FOO])

@router.get(
    "/agendamento", 
    response_model=List[schemas.AgendamentoBaseToUpload]
)
async def getAllData(
    page: int = 0, 
    per_page: int = -1,
):
    return getAllScheduling(page, per_page)

@router.get(
    "/agendamento/{id}",
    response_model=schemas.AgendamentoBaseToUpload
)
async def getData(id: int):
    return getscheduling(id)

@router.post(
    "/agendamento", 
    dependencies=[(Depends(enfCf))],
    response_model=schemas.AgendamentoBaseToUpload
)
async def postData(scheduling: schemas.AgendamentoCreated):
    return create_scheduling(scheduling)

@router.put(
    "/agendamento/{id}", 
    response_model=schemas.AgendamentoBaseToUpload,
    dependencies=[(Depends(enfCf))],
)
async def putData(
    id: int,
    scheduling: schemas.AgendamentoCreated
):
    return update_scheduling(id, scheduling)
    

@router.delete(
    "/agendamento/{id}",
    dependencies=[(Depends(enfCf))],
    response_model=schemas.AgendamentoBaseToUpload,
)
async def deleteData(id: int):
    return delete_scheduling(id)