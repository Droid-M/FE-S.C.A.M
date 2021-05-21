from os import path
import sys


sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.enfermeiroChefe import EnfermeiroChefeCreated
from fescam.model.EnfermeiroChefe import EnfermeiroChefe
from fescam.DAO.EnfermeiroChefeDAO import EnfermeiroChefeDAO

fake = Faker(['pt_BR'])

def factory():
    enfDAO = EnfermeiroChefeDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    enfermeiro = EnfermeiroChefeCreated(nome = nome, CPF = CPF, senha = senha)
    return enfDAO.createBySchema(enfermeiro)