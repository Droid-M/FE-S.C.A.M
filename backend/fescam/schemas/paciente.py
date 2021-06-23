from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, constr
from datetime import datetime, date

class Dado(BaseModel):
    nome_campo: str = ''
    valor_campo: str = ''

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
    
class tipoSexo(Enum):
    MASCULINO = 'MASCULINO'
    FEMININO = 'FEMININO'

class PacienteBase(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    sexo: Optional[tipoSexo]
    genero: Optional[genero]
    data_nascimento: Optional[date]
    tipo_sangue: Optional[tipoSangue]
    endereco: Optional[str]
    telefone: Optional[str]
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    nome_atendente: Optional[str] #<-- Rever isso
    dados: Optional[List[Dado]]
    
    class Config:
        use_enum_values = True

# Cria um paciente no sistema
class PacienteCreated(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    sexo: Optional[tipoSexo]
    genero: Optional[genero]
    data_nascimento: Optional[date]
    tipo_sangue: Optional[tipoSangue]
    endereco: Optional[str]
    telefone: Optional[str]
    nome_atendente: Optional[str] #<-- Rever isso
    dados: Optional[List[Dado]]
    
    class Config:
        use_enum_values = True


# Atualizar dados de diagnostico
class PacienteDadosUpload(PacienteBase):
    dados: List[Dado]
    
class PacienteStoreDB(BaseModel):
    CPF: constr(min_length=11, max_length=11)
    nome: str
    sexo: Optional[tipoSexo]
    genero: Optional[genero]
    data_nascimento: Optional[date]
    tipo_sangue: Optional[tipoSangue]
    endereco: Optional[str]
    telefone: Optional[str]
    nome_atendente: Optional[str] #<-- Rever isso
    
    class Config:
        use_enum_values = True