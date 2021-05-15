from backend.fescam.schemas.enfermeiro import EnfermeiroCreated
from backend.fescam.model.Enfermeiro import Enfermeiro
from backend.fescam.model.Funcionario import Funcionario
from backend.fescam.DAO.FuncionarioDAO import FuncionarioDAO
from backend.fescam.DAO.child.childBase import childBase

class EnfermeiroDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Enfermeiro, childSchemaCreated= EnfermeiroCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)