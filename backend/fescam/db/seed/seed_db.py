from datetime import datetime
import os
import random
from os import DirEntry, path
import sys

import fescam.db.factory.administrador_seed as administrador_seed
import fescam.db.factory.agendamento_seed as agendamento_seed
import fescam.db.factory.enfermeiro_seed as enfermeiro_seed
import fescam.db.factory.enfermerio_chefe_seed as enfermerio_chefe_seed
import fescam.db.factory.estagiario_seed as estagiario_seed
import fescam.db.factory.medicamento_seed as medicamento_seed
import fescam.db.factory.paciente_seed as paciente_seed
import fescam.db.factory.posologia_seed as posologia_seed
from fescam.db.create_schemas import create_all
from fescam.components.functions_helpers import create_file, makeDir, removeDir

DIRECTORY = os.path.abspath(__file__) + '/../../scripts/seed_result'

def dictToFileTXT(result: str, arq_title, write_mode:str = 'a+'):
    filePath = DIRECTORY + f'/{arq_title}.txt'
    if(create_file(filePath=filePath, content=result, writeMode=write_mode)):
        print(f"Informação inserida no arquivo {filePath}")

def seed():
    #Administrador
    max = random.randint(9, 13)
    arq_title = 'ADMINISTRADOR'
    result = ''
    for i in range(0, max, 1):
        print(' .')
        result += str(administrador_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
    #Enfermeiro
    max = random.randint(9, 13)
    result = ''
    arq_title = 'ENFERMEIRO'
    for i in range(0, max, 1):
        print(' .')
        result += str(enfermeiro_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
    #Estagiário
    max = random.randint(9, 13)
    result = ''
    arq_title = 'ESTAGIARIO'
    for i in range(0, max, 1):
        print(' .')
        result += str(estagiario_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
    #Enfermeiro chefe
    max = random.randint(3, 10)
    result = ''
    arq_title = 'ENFERMEIRO_CHEFE'
    for i in range(0, max, 1):
        print(' .')
        result += str(enfermerio_chefe_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
    
    #Paciente
    maxPac = random.randint(8, 24)
    arq_title = 'PACIENTE'
    result = ''
    for i in range(0, maxPac, 1):
        print(' .')
        result += str(paciente_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
    
    #Medicamento
    max = random.randint(40, 60)
    result = ''
    arq_title = 'MEDICAMENTO'
    for i in range(0, max, 1):
        print(' .')
        result += str(medicamento_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
    #Posologia
    arq_title = 'POSOLOGIA'
    result = ''
    for i in range(0, maxPac - 2, 1):
        print(' .')
        result += str(posologia_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
    #Agendamento
    arq_title = 'AGENDAMENTO'
    result = ''
    for i in range(0, maxPac - 2, 1):
        print(' .')
        result += str(agendamento_seed.factory())+'\n'
    dictToFileTXT(result, arq_title)
        
def prepare_DB():
    makeDir(DIRECTORY) #<Apenas por garantia
    create_all() #<- Cria as tabelas
    seed() #<- Semeia as tabelas

if __name__ == '__main__':
    prepare_DB()