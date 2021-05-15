from backend.fescam.schemas.estagiaro import EstagiarioCreated
from backend.fescam.model.Estagiario import Estagiario
from backend.fescam.model.Funcionario import Funcionario
from backend.fescam.DAO.FuncionarioDAO import FuncionarioDAO
from backend.fescam.DAO.child.childBase import childBase

class EstagiarioDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Estagiario, childSchemaCreated= EstagiarioCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)