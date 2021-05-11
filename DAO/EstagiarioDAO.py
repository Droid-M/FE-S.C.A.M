from schemas.estagiaro import EstagiarioCreated
from model.Estagiario import Estagiario
from model.Funcionario import Funcionario
from DAO.FuncionarioDAO import FuncionarioDAO
from DAO.child.childBase import childBase

class EstagiarioDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Estagiario, childSchemaCreated= EstagiarioCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)