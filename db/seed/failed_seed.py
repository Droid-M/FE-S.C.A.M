from faker import Faker
from components.functions_helpers import cpfNumber_int_to_str
from schemas.administrador import AdministradorCreated
from schemas.estagiaro import EstagiarioCreated
from model.Funcionario import Funcionario
from DAO.EstagiarioDAO import EstagiarioDAO

fake = Faker(['pt_BR'])

def estagiario_seed():
    estDAO = EstagiarioDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    estagiario = EstagiarioCreated(nome = nome, CPF = CPF, senha = senha)
    estDAO.createBySchema(estagiario)