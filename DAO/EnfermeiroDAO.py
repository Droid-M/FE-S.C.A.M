from schemas.enfermeiro import EnfermeiroCreated
from model.Enfermeiro import Enfermeiro
from model.Funcionario import Funcionario
from DAO.FuncionarioDAO import FuncionarioDAO
from DAO.child.childBase import childBase

class EnfermeiroDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Enfermeiro, childSchemaCreated= EnfermeiroCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)