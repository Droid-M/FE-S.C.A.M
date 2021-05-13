from typing import Optional
from pydantic import BaseModel, constr
from datetime import datetime

class EnfermeiroBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

# Cria um paciente no sistema
class EnfermeiroCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    senha: str