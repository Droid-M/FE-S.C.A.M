from fescam.db.execute_db_command import execute
from fescam.components.functions_helpers import read_file
#(falta definir a TIMEZONE)
import os

def create_all(): #<- Adicionar tratamento de exceção depois ****
    commands = read_file(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\init-database.sql")
    commands = (
        f"""
        {commands}
        """
        #is_active BOOLEAN DEFAULT TRUE <- Desnecessário
    )
    execute(commands)