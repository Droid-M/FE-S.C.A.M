import bcrypt
from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends
from fescam import DAO, model, schemas
from fescam.controller import PacienteController

posDAO = DAO.PosologiaDAO()
medDAO = DAO.MedicamentoDAO()

def getPosologieToUp(posologie: dict):
    if(posologie and len(posologie) > 0):
        posologie['medicamento'] = medDAO.findByPK(posologie['medicamento'], convert = False)
        posologie['paciente'] = PacienteController.getPatientDB(posologie['paciente'])
    return posologie

def getAllPosologies(
        page: int = 0, per_page: int = -1,
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            posologies = posDAO.getAll(convert = False)
            for posologie in posologies:
                getPosologieToUp(posologie)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(posologies)
                )
    else:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def getPosology(id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        posology = getPosologieToUp(posDAO.findByPK(id, convert = False))
        if(posology is not None and len(posology) > 0):
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(posology)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"id de posologia {id} não consta no sistema!"))
        )
    else:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def create_posology(
    posology: schemas.PosologiaCreated,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = getPosologieToUp(posDAO.createBySchema(posology, convert = False))
        if(result is not None and len(result) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(posology)
            )
        else:
            return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Falha ao salvar informações"))
        )
    else:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

def update_posology(
    id: int,
    posology: schemas.PosologiaCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        pos_updated = getPosologieToUp(posDAO.UPDATE(posology.dict()).WHERE("id", "=", id).getFirst())
        if(pos_updated is not None and len(pos_updated) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(pos_updated))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar uma posologia não cadastrada! ID:{id}")
            ))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def delete_posology(id: int):
    is_admin = True
    if(is_admin):
        deleted_pos = getPosologieToUp(posDAO.DeleteByPK(id, convert = False))
        if(deleted_pos is not None and len(deleted_pos) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(deleted_pos))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover uma posologia não cadastrada! ID:{id}")
        ))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")