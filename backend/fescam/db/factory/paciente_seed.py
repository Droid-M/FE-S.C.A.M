from os import path
import sys


sys.path.append(path.abspath('.'))

#from enum import Enum
from faker import Faker
from faker_enum import EnumProvider
from fescam.components.functions_helpers import cpfNumber_int_to_str
from fescam.model.Paciente import Paciente
from fescam.DAO.PacienteDAO import PacienteDAO
from fescam.DAO.EnfermeiroDAO import EnfermeiroDAO
from fescam.DAO.EnfermeiroChefeDAO import EnfermeiroChefeDAO
from fescam.DAO.EstagiarioDAO import EstagiarioDAO
from fescam.schemas.paciente import PacienteStoreDB, tipoSangue as TipoSangue, genero as Genero
import random

fake = Faker(['pt_BR'])
fake.add_provider(EnumProvider)
    
def factory():
    pacDAO = PacienteDAO()
    enfDAO = EnfermeiroDAO()
    enfCfDAO = EnfermeiroChefeDAO()
    #estDAO = EstagiarioDAO()
    enfermeiros = enfDAO.getAll()
    enferChefes = enfCfDAO.getAll()
    #estagiarios = estDAO.getAll()
    profSaude = enfermeiros + enferChefes
    index = random.randint(0, len(profSaude) - 1)
    atendente = profSaude[index]
    
    CPF = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    nome = fake.name()
    sexo = fake.boolean(chance_of_getting_true=50)
    genero = fake.enum(Genero)
    data_nascimento = fake.date_of_birth(tzinfo=None, minimum_age=16, maximum_age=99)
    tipo_sangue = fake.enum(TipoSangue)
    endereco = fake.address()
    telefone = cpfNumber_int_to_str(fake.pyint(min_value=0, max_value=99999999999, step=1))
    nome_atendente = atendente.nome
    
    paciente = PacienteStoreDB(
        CPF = CPF, 
        nome = nome, 
        sexo = sexo, 
        genero = genero,
        data_nascimento = data_nascimento,
        tipo_sangue = tipo_sangue,
        endereco = endereco,
        telefone = telefone,
        nome_atendente = nome_atendente,
        )
    result = pacDAO.createBySchema(paciente)
    if(bool(result)):
        return result.typesAcceptables
    return None
    