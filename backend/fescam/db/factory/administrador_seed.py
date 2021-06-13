from os import path
import sys

from pydantic.types import FilePath

sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.administrador import AdministradorCreated
from fescam.model.Administrador import Administrador
from fescam.DAO.AdministradorDAO import AdministradorDAO
import bcrypt

fake = Faker(['pt_BR'])

def factory():
    admDAO = AdministradorDAO()
    nome = fake.name()
    senha_original = fake.password(length=8, special_chars=False)
    senha = bcrypt.hashpw(senha_original.encode('utf-8'), bcrypt.gensalt()).decode()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    
    result = admDAO.createByTuple(nome = nome, CPF = CPF, senha = senha, tipo = 'ADMINISTRADOR')
    if(bool(result)):
        resultToDict = result.typesAcceptables
        resultToDict["senha"] = senha_original
        return resultToDict
    return None