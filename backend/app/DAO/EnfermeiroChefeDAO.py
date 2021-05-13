from backend.app.schemas.enfermeiroChefe import EnfermeiroChefeCreated
from backend.app.model.EnfermeiroChefe import EnfermeiroChefe
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.FuncionarioDAO import FuncionarioDAO
from backend.app.DAO.child.childBase import childBase

class EnfermeiroChefeDAO(childBase):
    def __init__(self):
        super().__init__(childModel= EnfermeiroChefe, childSchemaCreated= EnfermeiroChefeCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)