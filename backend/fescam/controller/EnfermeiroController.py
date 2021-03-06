from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, status
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


from fescam import DAO, model, schemas


funcDAO = DAO.FuncionarioDAO()
enfDAO = DAO.EnfermeiroDAO()

def read_all_enfermeiro(
        page: int = 0, per_page: int = -1,
        ): #-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        if(per_page > -1): #Se tem paginação definida:
            #users = funcDAO.getpagete(page, per_page) #Fazer método de paginação ***********
            pass
        else: #Senão, pega todos
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                content = jsonable_encoder(enfDAO.getAll(convert = False))
                )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")
    
def read_enfermeiro(enfermeiro_id: str):#-> Any
    is_admin = True #<- Fazer um tratamento pra saber se o usuário atual é admin ******* 
    if(is_admin):
        user = enfDAO.findByFK(enfermeiro_id)
        if(user is not None):
            nome = user.nome
            CPF = user.CPF
            created_on = user.created_on
            updated_on = user.updated_on
            user = schemas.EnfermeiroBase(
                nome = nome,
                CPF = CPF,
                created_on = created_on,
                updated_on = updated_on
                )
            return JSONResponse(
                status_code= status.HTTP_200_OK, 
                #description = 'Retorna uma lista de todos os usuários do sistema', 
                content = jsonable_encoder(user)
                )
        return JSONResponse(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            #description = f"ID/CPF de usuário {enfermeiro_id} não consta no sistema!",
            content= jsonable_encoder(schemas.Error(message = f"ID/CPF de usuário {enfermeiro_id} não consta no sistema!"))
        )
    else:
        #lance algum tipo de exceção ou redirecione, por exemplo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unexpected error")