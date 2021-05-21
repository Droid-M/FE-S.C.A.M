from os import path
import sys

sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.administrador import AdministradorCreated
from fescam.model.Administrador import Administrador
from fescam.DAO.AdministradorDAO import AdministradorDAO

fake = Faker(['pt_BR'])

def factory():
    admDAO = AdministradorDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    admistrador = AdministradorCreated(nome = nome, CPF = CPF, senha = senha)
    admDAO.createBySchema(admistrador)