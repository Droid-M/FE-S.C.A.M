from fescam.controller import PacienteController
from fescam.controller import FuncionarioController
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
enfCFDAO = DAO.EnfermeiroChefeDAO()
estDAO = DAO.EstagiarioDAO()

def getSchedulingToUp(scheduling: dict):
    if(scheduling is not None and len(scheduling) > 0):
        scheduling['posologia'] = posDAO.findByPK(scheduling['posologia'])
        scheduling['enfermeiro'] =  FuncionarioController.getFuncToUpload(scheduling['enfermeiro'], enfDAO)
        scheduling['estagiario'] = FuncionarioController.getFuncToUpload(scheduling['estagiario'], estDAO)
        scheduling['enferchefe'] = FuncionarioController.getFuncToUpload(scheduling['enferchefe'], enfCFDAO)
        scheduling['paciente'] = PacienteController.getPatientDB(scheduling['paciente'])
    return scheduling

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
                getSchedulingToUp(scheduling)
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
        scheduling = getSchedulingToUp(schDAO.findByPK(id, False))
        if(scheduling):
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
        result = getSchedulingToUp(schDAO.createBySchema(scheduling, convert = False))
        if(result is not None and len(result) > 0):
            #scheduling = schemas.AgendamentoBaseToUPload(**result.typesAcceptables)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(result)
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
        sch_updated = getSchedulingToUp(schDAO.UPDATE(scheduling.dict()).WHERE("id", "=", id).getFirst())
        if(sch_updated is not None and len(sch_updated) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(sch_updated))
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
        deleted_sch = getSchedulingToUp(schDAO.DeleteByPK(id, convert = False))
        if(deleted_sch is not None and len(deleted_sch) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(deleted_sch)
            )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover um agendamento não cadastrado! ID:{id}")
        ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")