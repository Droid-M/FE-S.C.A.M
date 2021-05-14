from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime, date

class PosologiaBase(BaseModel):
    id: int
    medicamento: int
    paciente: constr(min_length=11, max_length=11)
    quantidade: float
    notas: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

class PosologiaCreated(BaseModel):
    medicamento: int
    paciente: constr(min_length=11, max_length=11)
    quantidade: float
    notas: str
