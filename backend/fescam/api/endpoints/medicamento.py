from os import path
import bcrypt

from typing import Any, List, NoReturn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException, status, Depends

from fescam import DAO, model, schemas
from fescam.api.bearer import JWTBearer

router = APIRouter()
medDAO = DAO.MedicamentoDAO()

@router.get(
    "/medicamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=List[schemas.MedicamentoBase]
    ) 
async def getAllMedicaments(
        page: int = 0, per_page: int = -1,
        current_user: schemas.FuncionarioBase = None #usar alguma lógica pra pegar o usuário atual: Depends(deps.get_current_active_user)
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            medicals = medDAO.SELECT(['codigo', 'nome', 'created_on', 'updated_on'], convertReturn = False).getAll()
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(medicals)
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.get("/medicamento/{codigo}", 
            dependencies=[Depends(JWTBearer())], 
            response_model=schemas.MedicamentoBase)
async def getAllUsers(codigo: int):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        medicamento = medDAO.findByPK(codigo)
        if(medicamento is not None):
            medicamento = schemas.MedicamentoBase(**medicamento.typesAcceptables)
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(medicamento)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Código de medicamento {codigo} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.post(
    "/medicamento", 
    dependencies=[Depends(JWTBearer())],
    response_model=schemas.MedicamentoBase
    )
async def create_medicament(
    medicament: schemas.MedicamentoCreated,
    ): # -> Any
    is_admin = True
    if(is_admin):
        result = medDAO.createBySchema(medicament)
        if(result is not None):
            medicament = schemas.MedicamentoBase(**result.typesAcceptables)
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Um novo usuario foi cadastrado com sucesso', 
                content = jsonable_encoder(medicament)
            )
        else:
            return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Falha ao salvar informações"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.put("/medicamento/{codigo}", dependencies=[Depends(JWTBearer())])
async def update_medicament(
    codigo: int, 
    medicament: schemas.MedicamentoCreated,
): #-> Any
    #Buscando usuario:
    is_admin = True
    if(is_admin):
        med_updated = medDAO.UPDATE(medicament.dict()).WHERE("codigo", "=", codigo).getFirst()
        if(med_updated is not None and len(med_updated) > 0):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Atualização realizada com sucesso', 
                content = jsonable_encoder(schemas.MedicamentoBase(**med_updated)))
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível atualizar um medicamento não cadastrado! Código:{codigo}")
            ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")

@router.delete("/medicamento/{codigo}", dependencies=[Depends(JWTBearer())])
async def delete_user(codigo: int):
    is_admin = True
    if(is_admin):
        deleted_med = medDAO.DeleteByPK(codigo)
        if(deleted_med is not None):
            return JSONResponse(
                status_code = status.HTTP_200_OK,
                #description = 'Usuario deletado com sucesso', 
                content = jsonable_encoder(schemas.MedicamentoBase(**deleted_med.typesAcceptables))
            )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            content= jsonable_encoder(schemas.Error(message = f"Impossível remover um medicameto não cadastrado! Código:{codigo}")
        ))
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")