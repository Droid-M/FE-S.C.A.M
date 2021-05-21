from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class AgendamentoBase(BaseModel):
    id: int
    posologia: int
    paciente: constr(min_length=11, max_length=11)
    enferchefe: constr(min_length=11, max_length=11)
    enfermeiro: Optional[constr(min_length=11, max_length=11)] #<-- tratar para que apenas 1 ou outro seja escolhido **** -->
    estagiario: Optional[constr(min_length=11, max_length=11)]
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    horario: datetime

# criar um agendamento
class AgendamentoCreated(BaseModel): #Enfermeiro e estagiário podem ser alocados para o mesmo agendamento?
    posologia: int
    paciente: constr(min_length=11, max_length=11)
    enferchefe: constr(min_length=11, max_length=11)
    horario: datetime

# Adicionar um enfermeiro no agendamento
class AgendamentoAddEnf(AgendamentoCreated):
    enfermeiro: constr(min_length=11, max_length=11)

#Adicionar um estagiario no agendamento
class AgendamentoAddEst(AgendamentoCreated):
    estagiario: constr(min_length=11, max_length=11)