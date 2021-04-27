from execute_db_command import execute
#(falta definir a TIMEZONE)

def create_all(): #<- Adicionar tratamento de exceção depois ****
    commands = ''
    databaseFile = open("database.sql", "r")
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