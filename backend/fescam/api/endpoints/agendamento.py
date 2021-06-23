import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam.controller.AgendamentoController import *
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

@router.get(
    "/agendamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.AgendamentoBaseToUpload]
    )
async def getAllData(
    page: int = 0, 
    per_page: int = -1,
):
    return getAllScheduling(page, per_page)

@router.get("/agendamento/{id}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.AgendamentoBase)
async def getData(id: int):
    return getscheduling(id)

@router.post(
    "/agendamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase
    )
async def postData(scheduling: schemas.AgendamentoCreated):
    return create_scheduling(scheduling)

@router.put("/agendamento/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase
    )
async def putData(
    id: int,
    scheduling: schemas.AgendamentoCreated
):
    return update_scheduling(id, scheduling)
    

@router.delete("/agendamento/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase,
)
async def deleteData(id: int):
    return delete_scheduling(id)