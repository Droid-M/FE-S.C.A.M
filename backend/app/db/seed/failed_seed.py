from faker import Faker
from backend.app.components.functions_helpers import cpfNumber_int_to_str
from backend.app.schemas.administrador import AdministradorCreated
from backend.app.schemas.estagiaro import EstagiarioCreated
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.EstagiarioDAO import EstagiarioDAO

fake = Faker(['pt_BR'])

def estagiario_seed():
    estDAO = EstagiarioDAO()
    nome = fake.name()
    senha = fake.password()
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    estagiario = EstagiarioCreated(nome = nome, CPF = CPF, senha = senha)
    estDAO.createBySchema(estagiario)