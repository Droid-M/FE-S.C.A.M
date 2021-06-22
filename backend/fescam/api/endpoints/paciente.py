from os import path
import bcrypt

from typing import Any, List, NoReturn, Union
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends

from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()
patDAO = DAO.PacienteDAO()

@router.get(
    "/paciente", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.PacienteBase]
    ) 
async def getAllPatients(
        page: int = 0, per_page: int = -1,
        current_user: schemas.FuncionarioBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            patients = patDAO.getAll(convert = False)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(patients)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get("/paciente/{cpf}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.PacienteBase)
async def getPatient(cpf: str):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        patient = patDAO.findByPK(cpf)
        if(patient is not None):
            patient = schemas.PacienteBase(**patient.typesAcceptables)  #<-- Necessário? Rever
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(patient)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"CPF de paciente {cpf} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.post(
    "/paciente", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase
    )
async def create_patient(
    patient: schemas.PacienteCreated,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = patDAO.createBySchema(patient)
        if(result is not None):
            patient = schemas.PacienteBase(**result.typesAcceptables)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(patient)
            )
        else:
            return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Falha ao salvar informações"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.put("/paciente/{cpf}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase
)
async def update_patient(
    cpf:str,
    patient: Union[schemas.PacienteCreated, schemas.PacienteDadosUpload],
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        pat_updated = patDAO.UPDATE(patient.dict()).WHERE("cpf", "=", cpf).getFirst()
        if(pat_updated is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(schemas.PacienteBase(**pat_updated)))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar um paciente não cadastrado! CPF:{cpf}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/paciente/{cpf}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PacienteBase,
)
async def delete_patient(cpf: str):
    is_admin = True
    if(is_admin):
        deleted_pat = patDAO.DeleteByPK(cpf)
        if(deleted_pat is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(schemas.PacienteBase(**deleted_pat.typesAcceptables))
            )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover um paciente não cadastrado! CPF:{cpf}")
        ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")