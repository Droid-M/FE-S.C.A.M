from backend.app.schemas.administrador import AdministradorCreated
from backend.app.model.Administrador import Administrador
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
from backend.app.DAO.child.childBase import childBase

class AdministradorDAO(childBase):
    
    def __init__(self):
        super().__init__(childModel= Administrador, childSchemaCreated= AdministradorCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)