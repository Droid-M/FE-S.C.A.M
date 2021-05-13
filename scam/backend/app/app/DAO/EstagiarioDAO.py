from app.schemas.estagiaro import EstagiarioCreated
from app.model.Estagiario import Estagiario
from app.model.Funcionario import Funcionario
from app.DAO.FuncionarioDAO import FuncionarioDAO
from app.DAO.child.childBase import childBase

class EstagiarioDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Estagiario, childSchemaCreated= EstagiarioCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)