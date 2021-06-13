from os import path
import sys


sys.path.append(path.abspath('.'))

from enum import Enum
from faker import Faker
from faker_enum import EnumProvider
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.posologia import PosologiaCreated
from fescam.model.Posologia import Posologia
from fescam.DAO.PosologiaDAO import PosologiaDAO

from fescam.DAO.PacienteDAO import PacienteDAO
from fescam.DAO.MedicamentoDAO import MedicamentoDAO
import random

fake = Faker(['pt_BR'])
fake.add_provider(EnumProvider)
Notas = [
    'Checar batimentos', 
    'Aplicar doses em braços diferentes', 
    '', 
    'Injetar na testa' #kkk
    ] 
    
def factory():
    pacDAO = PacienteDAO()
    medDAO = MedicamentoDAO()
    posDAO = PosologiaDAO()
    pacientes = pacDAO.getAll()
    medicamentos = medDAO.getAll()
    index1 = random.randint(0, len(pacientes) - 1)
    index2 = random.randint(0, len(medicamentos) - 1)
    index3 = random.randint(0, len(Notas) - 1)
    paciente = pacientes[index1]
    medicamento = medicamentos[index2]
    
    paciente = paciente.CPF
    medicamento = medicamento.codigo
    quantidade = round(random.uniform(0.1, 72), 2)
    notas = Notas[index3]
    
    posologia = PosologiaCreated(
        medicamento = medicamento,
        quantidade = quantidade,
        notas = notas,
        paciente = paciente
        )
    result = posDAO.createBySchema(posologia)
    if(bool(result)):
        return result.typesAcceptables
    return None
    