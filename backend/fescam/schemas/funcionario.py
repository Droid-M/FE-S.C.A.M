from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime
from enum import Enum

class tipo(Enum):
    enfermeiro = 'ENFERMEIRO'
    estagiario = 'ESTAGIARIO'
    enfermeiro_chefe = 'ENFERMEIRO_CHEFE'
    administrador = 'ADMINISTRADOR'

class FuncionarioBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    tipo: tipo
    
    class Config:
        use_enum_values = True

# Cria um paciente no sistema
class FuncionarioCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    senha: str
    tipo: tipo
    
    class Config:
        use_enum_values = True

class Funcionario(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    senha: str
    
    class Config:
        use_enum_values = True
