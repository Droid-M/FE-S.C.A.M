from os import path
import sys
import bcrypt


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
    senha_original = fake.password(length=8, special_chars=False)
    senha = bcrypt.hashpw(senha_original.encode('utf-8'), bcrypt.gensalt()).decode()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    #enfermeiro = EnfermeiroChefeCreated(nome = nome, CPF = CPF, senha = senha)

    result = enfDAO.createByTuple(nome = nome, CPF = CPF, senha = senha, tipo = 'ENFERMEIRO_CHEFE')
    if(bool(result)):
        resultToDict = result.typesAcceptables
        resultToDict["senha"] = senha_original
        return resultToDict
    return None