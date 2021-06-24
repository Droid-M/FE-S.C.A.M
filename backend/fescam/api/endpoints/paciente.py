from typing import Any, List, NoReturn, Union
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import schemas
from fescam.components.functions_helpers import ENFERMEIRO_FOO, ESTAGIARIO_FOO, ADMINISTRADOR_FOO, ENFERMEIRO_CHEFE_FOO
from fescam.util import checkAccess
from fescam.controller.PacienteController import *

router = APIRouter()
enf_enfCf_auth = checkAccess.Check([ENFERMEIRO_CHEFE_FOO, ENFERMEIRO_FOO])

@router.get(
    "/paciente",
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
    response_model=schemas.PacienteBase
)
async def detData(cpf: str):
    return getPatient(cpf)

@router.post(
    "/paciente",
    dependencies=[Depends(enf_enfCf_auth)],
    response_model=schemas.PacienteBase
)
async def postData(patient: schemas.PacienteCreated):
    return create_patient(patient)

@router.put(
    "/paciente/{cpf}",
    dependencies=[Depends(enf_enfCf_auth)],
    response_model=schemas.PacienteBase
)
async def updateData(
    cpf: str,
    patient: Union[schemas.PacienteCreated, schemas.PacienteDadosUpload]
):
    return update_patient(cpf, patient)

@router.delete(
    "/paciente/{cpf}",
    dependencies=[Depends(enf_enfCf_auth)],
    response_model=schemas.PacienteBase,
)
async def deleteData(cpf: str):
    return delete_patient(cpf)