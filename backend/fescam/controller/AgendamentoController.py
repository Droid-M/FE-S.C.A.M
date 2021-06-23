from fescam.controller import PacienteController
import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

schDAO = DAO.AgendamentoDAO()
posDAO = DAO.PosologiaDAO()
enfDAO = DAO.EnfermeiroDAO()
estDAO = DAO.EstagiarioDAO()

def getFunc(cpf: str, dao):
    result = dao.findByFK(cpf)
    if(result):
        result = result.typesAcceptables
        result.pop('senha')
    return result

def getAllScheduling(
        page: int = 0, 
        per_page: int = -1,
        ): #-> Any
    is_admin = True 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            schedulings = schDAO.getAll(convert = False)
            for scheduling in schedulings:
                scheduling['posologia'] = posDAO.findByPK(scheduling['posologia'])
                scheduling['enfermeiro'] = getFunc(scheduling['enfermeiro'], enfDAO)
                scheduling['estagiario'] = getFunc(scheduling['estagiario'], estDAO)
                scheduling['paciente'] = PacienteController.getPatientDB(scheduling['paciente'])
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(schedulings)
            )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def getscheduling(id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        scheduling = schDAO.findByPK(id, False)
        if(scheduling is not None):
            scheduling['posologia'] = posDAO.findByPK(scheduling['posologia'])
            scheduling['enfermeiro'] = getFunc(scheduling['enfermeiro'], enfDAO)
            scheduling['estagiario'] = getFunc(scheduling['estagiario'], estDAO)
            scheduling['paciente'] = PacienteController.getPatientDB(scheduling['paciente'])
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(scheduling)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"id de agendamento {id} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def create_scheduling(scheduling: schemas.AgendamentoCreated): # -> Any
    is_admin = True
    if(is_admin):
        result = schDAO.createBySchema(scheduling)
        if(result is not None):
            scheduling = schemas.AgendamentoBase(**result.typesAcceptables)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(scheduling)
            )
        else:
            return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Falha ao salvar informações"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def update_scheduling(
    id: int,
    scheduling: schemas.AgendamentoCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        sch_updated = schDAO.UPDATE(scheduling.dict()).WHERE("id", "=", id).getFirst()
        if(sch_updated is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(schemas.AgendamentoBase(**sch_updated)))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar um agendamento não cadastrado! ID:{id}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def delete_scheduling(id: int):
    is_admin = True
    if(is_admin):
        deleted_sch = schDAO.DeleteByPK(id)
        if(deleted_sch is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(schemas.AgendamentoBase(**deleted_sch.typesAcceptables))
            )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover um agendamento não cadastrado! ID:{id}")
        ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")