from fescam.schemas.estagiario import EstagiarioCreated
from fescam.model.Estagiario import Estagiario
from fescam.model.Funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.DAO.child.childBase import childBase

class EstagiarioDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Estagiario, childSchemaCreated= EstagiarioCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)