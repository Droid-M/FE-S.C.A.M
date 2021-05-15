from backend.fescam.schemas.administrador import AdministradorCreated
from backend.fescam.model.Administrador import Administrador
from backend.fescam.model.Funcionario import Funcionario
from backend.fescam.DAO.FuncionarioDAO import FuncionarioDAO
from backend.fescam.DAO.child.childBase import childBase

class AdministradorDAO(childBase):
    
    def __init__(self):
        super().__init__(childModel= Administrador, childSchemaCreated= AdministradorCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)