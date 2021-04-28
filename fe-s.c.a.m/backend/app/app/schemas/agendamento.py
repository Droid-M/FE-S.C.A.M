from pydantic import BaseModel
from typing import Optional

class AgendamentoBase(BaseModel):
    enfermeiroChefe: int
    enfermeiro: Optional[int]
    estagiario: Optional[int]
    cpf_paciente: str
    posologia: int

# criar um agendamento
class AgendamentoCreate(AgendamentoBase):
    enfermeiroChefe: int
    enfermeiro: Optional[int] = None
    estagiario: Optional[int] = None
    cpf_paciente: str
    posologia: int


# Adicionar um enfermeiro no agendamento
class AgendamentoAddEnf(AgendamentoBase):
    enfermeiro: Optional[int]= None

#Adicionar um estagiario no agendamento
class AgendamentoAddEst(AgendamentoBase):
    estagiario: Optional[int]= None

