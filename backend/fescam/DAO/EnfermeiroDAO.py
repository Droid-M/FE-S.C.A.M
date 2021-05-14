from fescam.schemas.enfermeiro import EnfermeiroCreated
from fescam.model.Enfermeiro import Enfermeiro
from fescam.model.Funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.DAO.child.childBase import childBase

class EnfermeiroDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Enfermeiro, childSchemaCreated= EnfermeiroCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)