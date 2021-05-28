from fescam.db.execute_db_command import execute
from fescam.components.functions_helpers import read_file
import io
#(falta definir a TIMEZONE)
import os

def create_types(): #<- Adicionar tratamento de exceção depois ****
    commands = ''
    databaseFile = io.open(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\types.sql", "r", encoding="utf8")
    for line in databaseFile:
        commands += line
    databaseFile.close()  
    commands = (
        f"""
        {commands}
        """
        #is_active BOOLEAN DEFAULT TRUE <- Desnecessário
    )
    execute(commands)

def create_tables(): #<- Adicionar tratamento de exceção depois ****
    commands = ''
    databaseFile = io.open(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\tables.sql", "r", encoding="utf8")
    for line in databaseFile:
        commands += line
    databaseFile.close()  
    commands = (
        f"""
        {commands}
        """
        #is_active BOOLEAN DEFAULT TRUE <- Desnecessário
    )
    execute(commands)
    
def create_all(): #<- Adicionar tratamento de exceção depois ****
    commands = read_file(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\init-database.sql")
    commands = (
        f"""
        {commands}
        """
        #is_active BOOLEAN DEFAULT TRUE <- Desnecessário
    )
    execute(commands)