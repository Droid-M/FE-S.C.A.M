from app.schemas.enfermeiroChefe import EnfermeiroChefeCreated
from app.model.EnfermeiroChefe import EnfermeiroChefe
from app.model.Funcionario import Funcionario
from app.DAO.FuncionarioDAO import FuncionarioDAO
from app.DAO.child.childBase import childBase

class EnfermeiroChefeDAO(childBase):
    def __init__(self):
        super().__init__(childModel= EnfermeiroChefe, childSchemaCreated= EnfermeiroChefeCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)