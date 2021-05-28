import os
from fescam.components.functions_helpers import read_file, create_file, lstrListToStr

from fescam.DAO import AdministradorDAO, EnfermeiroChefeDAO, EnfermeiroDAO, EstagiarioDAO, FuncionarioDAO, MedicamentoDAO, PacienteDAO, PosologiaDAO, AgendamentoDAO

from fescam.model import Administrador, Agendamento, EnfermeiroChefe, Enfermeiro, Estagiario, Funcionario, Medicamento, Paciente, Posologia

def convert_values(list):
        result = ''
        for item in list:
            result += f"'{item}'," if(item is not None) else 'NULL,'
        return result[:-1] #<-- Removendo ultima vírgula

def inserts_generator(schemaName:str, dao, model):
    script = ""
    result = dao.getAll(convert = False, disassociate = True)
    tableName = model.tableName
    for data in result:
        atributes = lstrListToStr(data.keys(), ",")
        values = convert_values(data.values())
        script += f"\nINSERT INTO {schemaName}.{tableName}({atributes}) VALUES ({values});"
    return script

def backup(filePath:str):
    script = read_file(os.path.dirname(os.path.abspath(__file__)) + "/scripts/init-database.sql", "insert into")
    #script = read_file(os.path.dirname(os.path.abspath(__file__)) + "\\scripts\\init-database.sql", "insert into") <-- Windows
    models = [
        Funcionario, 
        Administrador, 
        Enfermeiro, 
        EnfermeiroChefe, 
        Estagiario,
        Paciente,
        Medicamento,
        Posologia,
        Agendamento
    ]
    
    DAOs = [
        FuncionarioDAO,
        AdministradorDAO,
        EnfermeiroDAO,
        EnfermeiroChefeDAO,
        EstagiarioDAO,
        PacienteDAO,
        MedicamentoDAO,
        PosologiaDAO,
        AgendamentoDAO
    ]
    
    #Obs. importante: 'models' e 'DAOs' precisam ter componentes respectivos e na mesma quantidade *******
    for model, dao in zip(models, DAOs):
        script += inserts_generator(
            schemaName= "public", #<-- Fazer tratamento pra pegar o nome automaticamente depois ******
            dao= dao(),
            model= model()
    )
    return create_file(filePath, script)