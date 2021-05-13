from backend.app.schemas.estagiaro import EstagiarioCreated
from backend.app.model.Estagiario import Estagiario
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
from backend.app.DAO.child.childBase import childBase

class EstagiarioDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Estagiario, childSchemaCreated= EstagiarioCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)