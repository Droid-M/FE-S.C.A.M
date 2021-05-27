from fescam.db.execute_db_command import execute
#(falta definir a TIMEZONE)
import os

def create_types(): #<- Adicionar tratamento de exceção depois ****
    commands = ''
    databaseFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\types.sql", "r")
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
    databaseFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\tables.sql", "r")
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
    commands = ''
    databaseFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\init-database.sql", "r")
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