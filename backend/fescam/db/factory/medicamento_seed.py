from os import path
import sys


sys.path.append(path.abspath('.'))
import random
from faker import Faker
from fescam.schemas.medicamento import MedicamentoCreated
from fescam.model.Medicamento import Medicamento
from fescam.DAO.MedicamentoDAO import MedicamentoDAO

fake = Faker(['pt_BR'])

def factory():
    comp = random.randint(0, 999999)
    medDAO = MedicamentoDAO()
    nome = "medicamento_" + str(comp)
    codigo = fake.pyint(min_value=0, max_value=9999999999, step=1)
    medicamento = MedicamentoCreated(nome = nome, codigo = codigo)
    result = medDAO.createBySchema(medicamento)
    if(bool(result)):
        return result.typesAcceptables
    return None