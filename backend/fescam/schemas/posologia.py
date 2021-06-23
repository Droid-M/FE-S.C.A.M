from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime, date
from .medicamento import MedicamentoBase
from .paciente import PacienteBase

class PosologiaBase(BaseModel):
    id: int
    medicamento: int
    paciente: constr(min_length=11, max_length=11)
    quantidade: float
    notas: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    
    class Config:
        use_enum_values = True

class PosologiaCreated(BaseModel):
    medicamento: int
    paciente: constr(min_length=11, max_length=11)
    quantidade: float
    notas: str
    
    class Config:
        use_enum_values = True
        
class PosologiaToUpload(BaseModel):
    id: int
    medicamento: MedicamentoBase
    paciente: PacienteBase
    quantidade: float
    notas: str
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    
    class Config:
        use_enum_values = True