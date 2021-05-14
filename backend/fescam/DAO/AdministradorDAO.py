from fescam.schemas.administrador import AdministradorCreated
from fescam.model.Administrador import Administrador
from fescam.model.Funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.DAO.child.childBase import childBase

class AdministradorDAO(childBase):
    
    def __init__(self):
        super().__init__(childModel= Administrador, childSchemaCreated= AdministradorCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)