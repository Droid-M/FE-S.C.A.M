from app.schemas.enfermeiro import EnfermeiroCreated
from app.model.Enfermeiro import Enfermeiro
from app.model.Funcionario import Funcionario
from app.DAO.FuncionarioDAO import FuncionarioDAO
from app.DAO.child.childBase import childBase

class EnfermeiroDAO(childBase):
    def __init__(self):
        super().__init__(childModel= Enfermeiro, childSchemaCreated= EnfermeiroCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)