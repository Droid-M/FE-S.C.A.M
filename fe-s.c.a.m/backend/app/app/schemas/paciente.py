from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class PacienteBase(BaseModel):
    CPF: str
    nome: str
    sexo: bool
    tipoSangue: Enum
    dataNascimento: str
    endereco: str
    telefone: str
    genero: Enum
    createdOn: datetime 
    updatedOn: datetime 
    enfermeiro_id: int

class PacienteCreated(BaseModel):
    CPF: str
    nome: str
    sexo: bool
    tipoSangue: Enum
    dataNascimento: str
    endereco: str
    telefone: str
    genero: Enum
    dados: str
    enfermeiro_id: int




