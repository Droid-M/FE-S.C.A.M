from typing import Any, List, NoReturn, Union
import bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer
from fescam.controller.PacienteController import *

patDAO = DAO.PacienteDAO()
dataDAO = DAO.DadosPacienteDAO()

#_________________ informações extra/observações do prontuário _________________#
def getPatientData(CPF: str):
    return dataDAO.SELECT([
        'nome_campo', 'valor_campo'
    ]).WHERE('paciente', '=', CPF).getAll()

def deletePatientData(cpf: str):
    return dataDAO.DELETE().WHERE('paciente', '=', cpf).getFirst()

def insertPatientData(cpf, data: List[dict]):
    if(data):
        for d in data:
            d['paciente'] = cpf
            dataDAO.INSERT(d)

def updatePatientData(cpf, data: List[dict]):
    deletePatientData(cpf)
    insertPatientData(cpf, data)

#_________________ Informações principais do paciente _________________#

def getAllPatients(
        page: int = 0,
        per_page: int = -1,
        current_user: schemas.FuncionarioBase = None
):  # -> Any
    is_admin = True
    if(is_admin):
        if(per_page > -1):
            pass
        else:
            patients = patDAO.getAll(convert=False)
            for patient in patients:
                patient["dados"] = getPatientData(patient['CPF'])
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                #description = 'Retorna uma lista de todos os usuários do sistema',
                content=jsonable_encoder(patients)
            )
    else:
        # lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")


def getPatient(cpf: str):  # -> Any
    is_admin = True  # <- Fazer um tratamento pra saber se o usuário atual é admin *******
    if(is_admin):
        patient = patDAO.findByPK(cpf)
        if(patient is not None):
            patient = schemas.PacienteBase(
                **patient.typesAcceptables, 
                dados=getPatientData(patient.CPF)
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                #description = 'Retorna uma lista de todos os usuários do sistema',
                content=jsonable_encoder(patient)
            )
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content=jsonable_encoder(schemas.Error(
                message=f"CPF de paciente {cpf} não consta no sistema!"))
        )
    else:
        # lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")


def create_patient(
    patient: schemas.PacienteCreated,
):  # -> Any
    is_admin = True
    if(is_admin):
        patient = patient.dict()
        data = patient.pop('dados', None)
        result = patDAO.createByTuple(**patient)
        if(result is not None):
            insertPatientData(result.CPF, data)
            patient = schemas.PacienteBase(
                **result.typesAcceptables,
                dados=getPatientData(result.CPF))
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso',
                content=jsonable_encoder(patient)
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                content=jsonable_encoder(schemas.Error(
                    message=f"Falha ao salvar informações"))
            )
    else:
        # lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

def update_patient(
    cpf: str,
    patient: schemas.PacienteCreated,
):  # -> Any
    # Buscando usuario:
    is_admin = True
    if(is_admin):
        patient = patient.dict()
        updatePatientData(cpf, patient.pop('dados', None))
        pat_updated = patDAO.UPDATE(patient).WHERE(
            "cpf", "=", cpf).getFirst()
        if(pat_updated is not None and len(pat_updated) > 0):
            pat_updated['dados'] = getPatientData(pat_updated['CPF'])
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso',
                content=jsonable_encoder(schemas.PacienteBase(**pat_updated)))
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content=jsonable_encoder(schemas.Error(message=f"Impossível atualizar um paciente não cadastrado! CPF:{cpf}")
                                     ))
    else:
        # lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")


def delete_patient(cpf: str):
    is_admin = True
    if(is_admin):
        data = getPatientData(cpf)
        deleted_pat = patDAO.DeleteByPK(cpf)
        if(deleted_pat is not None):
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso',
                content=jsonable_encoder(schemas.PacienteBase(
                    **deleted_pat.typesAcceptables,
                    dados = data))
            )
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content=jsonable_encoder(schemas.Error(message=f"Impossível remover um paciente não cadastrado! CPF:{cpf}")
                                     ))
    else:
        # lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
