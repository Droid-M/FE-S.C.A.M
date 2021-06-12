from fescam.schemas import posologia
from os import path
import bcrypt

from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends

from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()
posDAO = DAO.PosologiaDAO()

@router.get(
    "/posologia", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.PosologiaBase]
    ) 
async def getAllPosologies(
        page: int = 0, per_page: int = -1,
        current_user: schemas.FuncionarioBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            posologies = posDAO.getAll(convert = False)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(posologies)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get("/posologia/{id}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.PosologiaBase)
async def getPosology(id: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        posology = posDAO.findByPK(id)
        if(posology is not None):
            posology = schemas.PosologiaBase(**posology.typesAcceptables)  #<-- Necessário? Rever
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
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.post(
    "/posologia", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase
    )
async def create_posology(
    posology: schemas.PosologiaCreated,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = posDAO.createBySchema(posology)
        if(result is not None):
            posology = schemas.PosologiaBase(**result.typesAcceptables)
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
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.put("/posologia/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase
    )
async def update_posology(
    id: int,
    posology: schemas.PosologiaCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        pos_updated = posDAO.UPDATE(posology.dict()).WHERE("id", "=", id).getFirst()
        if(pos_updated is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(schemas.PosologiaBase(**pos_updated.typesAcceptables)))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar uma posologia não cadastrada! ID:{id}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/posologia/{id}", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.PosologiaBase,
)
async def delete_posology(id: int):
    is_admin = True
    if(is_admin):
        deleted_pos = posDAO.DeleteByPK(id)
        if(deleted_pos is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(schemas.PosologiaBase(**deleted_pos.typesAcceptables))
            )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover uma posologia não cadastrada! ID:{id}")
        ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")