from typing import Optional

from fastapi import FastAPI, Response, status
from pydantic import BaseModel


class Error(BaseModel):
    code: int = 500
    message: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/enfermeirochefe/")
def read_all_enfermeirochefe(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/enfermeirochefe/{enfermeiro_chefe_id}')
def read_enfermeirochefe(enfermeiro_chefe_id: int, response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/enfermeiro')
def read_all_enfermeiro(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/enfermeiro/{enfermeiro_id}')
def read_enfermeiro(enfermeiro_id: int, response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/administrador')
def read_all_administrador(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/administrador/{administrador_id}')
def read_enfermeiro(administrador_id: int, response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.get('/agendamento_enfermeiro_chefe')
def read_all_agendamento_enfermeiro_chefe(response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')

@app.post('/agendamento_enfermeiro_chefe/{id}/{posologia}')

@app.get('/administrador/{administrador_id}')
def read_enfermeiro(administrador_id: int, response: Response):
    response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return Error(message='Not implemented')