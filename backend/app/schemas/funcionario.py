from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime

class FuncionarioBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

# Cria um paciente no sistema
class FuncionarioCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    senha: str

class Funcionario(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    senha: str
