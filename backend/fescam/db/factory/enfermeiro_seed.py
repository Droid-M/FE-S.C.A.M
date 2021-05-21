from os import path
import sys


sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.enfermeiro import EnfermeiroCreated
from fescam.model.Enfermeiro import Enfermeiro
from fescam.DAO.EnfermeiroDAO import EnfermeiroDAO

fake = Faker(['pt_BR'])

def factory():
    enfDAO = EnfermeiroDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    enfermeiro = EnfermeiroCreated(nome = nome, CPF = CPF, senha = senha)
    return enfDAO.createBySchema(enfermeiro)