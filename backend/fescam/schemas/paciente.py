from typing import Optional
from enum import Enum
from pydantic import BaseModel, constr
from datetime import datetime, date

class tipoSangue(Enum):
    AP = 'a+'
    AN = 'a-'
    BP = 'b+'
    BN = 'b-'
    ABP = 'ab+'
    ABN = 'ab-'
    OP = 'o+'
    ON = 'o-'
    NULLH = 'null_rh'
    
class genero(Enum):
    cis = 'cis'
    trans = 'trans'
    nonB = 'non-b'

class PacienteBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    sexo: Optional[bool]
    genero: Optional[genero]
    data_nascimento: Optional[date]
    tipo_sangue: Optional[tipoSangue]
    endereco: Optional[str]
    telefone: Optional[str]
    created_on: Optional[datetime]
    updated_on: Optional[datetime] 
    enfermeiro_id: constr(min_length=11, max_length=11) #<-- Rever isso
    dados: Optional[str]
    
    class Config:
        use_enum_values = True

# Cria um paciente no sistema
class PacienteCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    sexo: Optional[bool]
    genero: Optional[genero]
    data_nascimento: Optional[date]
    tipo_sangue: Optional[tipoSangue]
    endereco: Optional[str]
    telefone: Optional[str]
    enfermeiro_id: constr(min_length=11, max_length=11) #<-- Rever isso
    dados: Optional[str]
    
    class Config:
        use_enum_values = True


# Atualizar dados de diagnostico
class PacienteDadosUpload(PacienteBase):
    dados: str




