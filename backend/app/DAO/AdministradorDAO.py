from app.schemas.administrador import AdministradorCreated
from app.model.Administrador import Administrador
from app.model.Funcionario import Funcionario
from app.DAO.FuncionarioDAO import FuncionarioDAO
from app.DAO.child.childBase import childBase

class AdministradorDAO(childBase):
    
    def __init__(self):
        super().__init__(childModel= Administrador, childSchemaCreated= AdministradorCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)