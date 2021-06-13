from os import path
import sys
import bcrypt


sys.path.append(path.abspath('.'))
from faker import Faker
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.schemas.estagiaro import EstagiarioCreated
from fescam.model.Funcionario import Funcionario
from fescam.DAO.EstagiarioDAO import EstagiarioDAO

fake = Faker(['pt_BR'])

def factory():
    estDAO = EstagiarioDAO()
    nome = fake.name()
    senha_original = fake.password(length=8, special_chars=False)
    senha = bcrypt.hashpw(senha_original.encode('utf-8'), bcrypt.gensalt()).decode()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    #estagiario = EstagiarioCreated(nome = nome, CPF = CPF, senha = senha)
    
    result = estDAO.createByTuple(nome = nome, CPF = CPF, senha = senha, tipo = 'ESTAGIARIO')
    if(bool(result)):
        resultToDict = result.typesAcceptables
        resultToDict["senha"] = senha_original
        return resultToDict
    return None
