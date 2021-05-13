from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime

class EstagiarioBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

# Cria um paciente no sistema
class EstagiarioCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    senha: str