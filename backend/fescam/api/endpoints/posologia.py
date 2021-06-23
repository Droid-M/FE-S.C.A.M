import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam.controller.PosologiaController import *
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()

@router.get(
    "/posologia", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.PosologiaBase]
    ) 
async def getAllData(page: int = 0, per_page: int = -1):
    return getAllPosologies(page, per_page)

@router.get("/posologia/{id}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.PosologiaBase)
async def getData(id: int):
    return getPosology(id)

@router.post(
    "/posologia", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase
    )
async def postData(posology: schemas.PosologiaCreated):
    return create_posology(posology)

@router.put("/posologia/{id}",
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase
    )
async def putData(
    id: int,
    posology: schemas.PosologiaCreated,
):
    return update_posology(id, posology)

@router.delete("/posologia/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase,
)
async def deleteData(id: int):
    return delete_posology(id)