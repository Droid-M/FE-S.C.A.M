from os import path
import bcrypt

from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends

from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()
schDAO = DAO.AgendamentoDAO()

@router.get(
    "/agendamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.AgendamentoBase]
    )
async def getAllScheduling(
        page: int = 0, per_page: int = -1,
        current_user: schemas.FuncionarioBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            scheduling = schDAO.getAll(convert = False)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(scheduling)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get("/agendamento/{id}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.AgendamentoBase)
async def getscheduling(id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        scheduling = schDAO.findByPK(id)
        if(scheduling is not None):
            scheduling = schemas.AgendamentoBase(**scheduling.typesAcceptables)  #<-- Necessário? Rever
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

@router.post(
    "/agendamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase
    )
async def create_scheduling(
    scheduling: schemas.AgendamentoCreated,
    ): # -> Any
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

@router.put("/agendamento/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase
    )
async def update_scheduling(
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
                content = jsonable_encoder(schemas.AgendamentoBase(**sch_updated.typesAcceptables)))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar um agendamento não cadastrado! ID:{id}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/agendamento/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.AgendamentoBase,
)
async def delete_scheduling(id: int):
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