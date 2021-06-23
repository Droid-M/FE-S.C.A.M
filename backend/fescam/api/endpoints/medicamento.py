import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer
from fescam.controller.MedicamentoController import *

router = APIRouter()

@router.get(
    "/medicamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.MedicamentoBase]
    ) 
async def getAllData(page: int = 0, per_page: int = -1):
    return getAllMedicaments(page, per_page)

@router.get("/medicamento/{codigo}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.MedicamentoBase)
async def getData(codigo: str):
    return getMedicament(codigo)

@router.post(
    "/medicamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.MedicamentoBase
    )
async def postData(medicament: schemas.MedicamentoCreated):
    return create_medicament(medicament)

@router.put("/medicamento/{codigo}", dependencies=[Depends(JWTBearer())])
async def putData(
    codigo: str, 
    medicament: schemas.MedicamentoCreated,
):
    return update_medicament(codigo, medicament)

@router.delete("/medicamento/{codigo}", dependencies=[Depends(JWTBearer())])
async def deleteData(codigo: str):
    return delete_Medicament(codigo)