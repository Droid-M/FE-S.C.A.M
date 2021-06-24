import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import DAO, model, schemas
from fescam.components.functions_helpers import ENFERMEIRO_FOO, ESTAGIARIO_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_CHEFE_FOO
from fescam.controller.MedicamentoController import *
from fescam.util import checkAccess

router = APIRouter()
enfCf_auth = checkAccess.Check([ENFERMEIRO_CHEFE_FOO])

@router.get(
    "/medicamento", 
    response_model=List[schemas.MedicamentoBase]
) 
async def getAllData(page: int = 0, per_page: int = -1):
    return getAllMedicaments(page, per_page)

@router.get(
    "/medicamento/{codigo}", 
    response_model=schemas.MedicamentoBase
)
async def getData(codigo: str):
    return getMedicament(codigo)

@router.post(
    "/medicamento", 
    dependencies=[Depends(enfCf_auth)],
    response_model=schemas.MedicamentoBase
)
async def postData(medicament: schemas.MedicamentoCreated):
    return create_medicament(medicament)

@router.put(
    "/medicamento/{codigo}",
    dependencies=[Depends(enfCf_auth)],
)
async def putData(
    codigo: str,
    medicament: schemas.MedicamentoCreated,
):
    return update_medicament(codigo, medicament)

@router.delete(
    "/medicamento/{codigo}",
    dependencies=[Depends(enfCf_auth)],
)
async def deleteData(codigo: str):
    return delete_Medicament(codigo)