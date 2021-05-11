from schemas.administrador import AdministradorCreated
from model.Administrador import Administrador
from model.Funcionario import Funcionario
from DAO.FuncionarioDAO import FuncionarioDAO
from DAO.child.childBase import childBase

class AdministradorDAO(childBase):
    
    def __init__(self):
        super().__init__(childModel= Administrador, childSchemaCreated= AdministradorCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)