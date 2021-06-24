from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class MedicamentoBase(BaseModel):
    codigo:str
    nome: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

class MedicamentoCreated(BaseModel):
    codigo: str
    nome: str

    