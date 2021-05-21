from os import path
import sys


sys.path.append(path.abspath('.'))

from faker import Faker
from fescam.schemas.agendamento import AgendamentoAddEnf
from fescam.schemas.agendamento import AgendamentoAddEst
from fescam.model.Agendamento import Agendamento
from fescam.DAO.AgendamentoDAO import AgendamentoDAO
from fescam.DAO.PosologiaDAO import PosologiaDAO
from fescam.DAO.PacienteDAO import PacienteDAO
from fescam.DAO.EnfermeiroDAO import EnfermeiroDAO
from fescam.DAO.EnfermeiroChefeDAO import EnfermeiroChefeDAO
from fescam.DAO.EstagiarioDAO import EstagiarioDAO
import random

fake = Faker(['pt_BR'])
    
def factory():
    agdDAO = AgendamentoDAO()
    pacDAO = PacienteDAO()
    posDAO = PosologiaDAO()
    enfDAO = EnfermeiroDAO()
    enfCfDAO = EnfermeiroChefeDAO()
    estDAO = EstagiarioDAO()
    
    pacientes = pacDAO.getAll()
    enfermeiros = enfDAO.getAll()
    enferChefes = enfCfDAO.getAll()
    estagiarios = estDAO.getAll()
    posologias = posDAO.getAll()
    
    profEscolhido = fake.boolean(chance_of_getting_true=65)
    
    index1 = random.randint(0, len(pacientes) - 1)
    index2 = random.randint(0, len(enferChefes) - 1)
    index3 = random.randint(0, len(posologias) - 1)
    index4 = random.randint(0, len(enfermeiros) - 1)
    index5 = random.randint(0, len(estagiarios) - 1)
    
    paciente = pacientes[index1]
    enferChefe = enferChefes[index2]
    posologia = posologias[index3]
    enfermeiro = enfermeiros[index4]
    estagiario = estagiarios[index5]
    
    posologia = posologia.id
    paciente = paciente.CPF
    enferchefe = enferChefe.CPF
    enfermeiro = enfermeiro.CPF if(profEscolhido) else None
    estagiario = estagiario.CPF if(not profEscolhido) else None
    horario = fake.date_time()
    
    agendamento = None
    if(profEscolhido):
        agendamento = AgendamentoAddEnf(
            posologia = posologia,
            paciente = paciente,
            enferchefe = enferchefe,
            enfermeiro = enfermeiro,
            horario = horario
        )
    else:
        agendamento = AgendamentoAddEst(
            posologia = posologia,
            paciente = paciente,
            enferchefe = enferchefe,
            estagiario = estagiario,
            horario = horario
        )
    agdDAO.createBySchema(agendamento)
    