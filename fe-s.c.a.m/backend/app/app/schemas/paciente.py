from typing import Optional
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
    updatedOn: Optional[datetime] 
    enfermeiro_id: int

# Cria um paciente no sistema
class PacienteCreated(PacienteBase):
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


# Atualizar dados de diagnostico
class PacienteDadosUpload(PacienteBase):
    dados: str




