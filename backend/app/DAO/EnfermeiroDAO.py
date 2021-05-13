from backend.app.schemas.enfermeiro import EnfermeiroCreated
from backend.app.model.Enfermeiro import Enfermeiro
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
from backend.app.DAO.child.childBase import childBase

class EnfermeiroDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Enfermeiro, childSchemaCreated= EnfermeiroCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)