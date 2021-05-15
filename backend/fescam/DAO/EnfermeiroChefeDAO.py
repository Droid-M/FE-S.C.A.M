from backend.fescam.schemas.enfermeiroChefe import EnfermeiroChefeCreated
from backend.fescam.model.EnfermeiroChefe import EnfermeiroChefe
from backend.fescam.model.Funcionario import Funcionario
from backend.fescam.DAO.FuncionarioDAO import FuncionarioDAO
from backend.fescam.DAO.child.childBase import childBase

class EnfermeiroChefeDAO(childBase):
    def __init__(self):
        super().__init__(childModel= EnfermeiroChefe, childSchemaCreated= EnfermeiroChefeCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)