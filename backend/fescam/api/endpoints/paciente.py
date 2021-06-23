from typing import Any, List, NoReturn, Union
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import schemas
from fescam.api.bearer import JWTBearer
from fescam.controller.PacienteController import *

router = APIRouter()

@router.get(
    "/paciente",
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.PacienteBase]
)
async def getAllData(
    page: int = 0,
    per_page: int = -1,
    current_user: schemas.FuncionarioBase = None
):
    return getAllPatients(page, per_page, current_user)

@router.get(
    "/paciente/{cpf}",
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase
)
async def detData(cpf: str):
    return getPatient(cpf)

@router.post(
    "/paciente",
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase
)
async def postData(patient: schemas.PacienteCreated):
    return create_patient(patient)

@router.put(
    "/paciente/{cpf}",
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase
)
async def updateData(
    cpf: str,
    patient: Union[schemas.PacienteCreated, schemas.PacienteDadosUpload]
):
    return update_patient(cpf, patient)

@router.delete("/paciente/{cpf}",
               dependencies=[Depends(JWTBearer())],
               response_model=schemas.PacienteBase,
               )
async def deleteData(cpf: str):
    return delete_patient(cpf)
