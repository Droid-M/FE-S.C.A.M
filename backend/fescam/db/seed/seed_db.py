import random
from os import path
import sys

sys.path.append(path.abspath('.'))

import fescam.db.factory.administrador_seed as administrador_seed
import fescam.db.factory.agendamento_seed as agendamento_seed
import fescam.db.factory.enfermeiro_seed as enfermeiro_seed
import fescam.db.factory.enfermerio_chefe_seed as enfermerio_chefe_seed
import fescam.db.factory.estagiario_seed as estagiario_seed
import fescam.db.factory.medicamento_seed as medicamento_seed
import fescam.db.factory.paciente_seed as paciente_seed
import fescam.db.factory.posologia_seed as posologia_seed
from fescam.db.create_schemas import create_all

def seed():
    #Administrador
    
    #Enfermeiro
    max = random.randint(9, 13)
    for i in range(0, max, 1):
        enfermeiro_seed.factory()
        
    #Estagiário
    max = random.randint(9, 13)
    for i in range(0, max, 1):
        estagiario_seed.factory()
        
    #Enfermeiro chefe
    max = random.randint(3, 10)
    for i in range(0, max, 1):
        enfermerio_chefe_seed.factory()
    
    #Paciente
    maxPac = random.randint(8, 24)
    for i in range(0, maxPac, 1):
        paciente_seed.factory()
    
    #Medicamento
    max = random.randint(40, 60)
    for i in range(0, max, 1):
        medicamento_seed.factory()
        
    #Posologia
    for i in range(0, maxPac - 2, 1):
        posologia_seed.factory()
        
    #Agendamento
    for i in range(0, maxPac - 2, 1):
        agendamento_seed.factory()
        
def prepare_DB():
    create_all() #<- Cria as tabelas
    seed() #<- Semeia as tabelas
    
if __name__ == '__main__':
    prepare_DB()