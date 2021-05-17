from fescam.schemas.enfermeiroChefe import EnfermeiroChefeCreated
from fescam.model.EnfermeiroChefe import EnfermeiroChefe
from fescam.model.Funcionario import Funcionario
from fescam.DAO.FuncionarioDAO import FuncionarioDAO
from fescam.DAO.child.childBase import childBase

class EnfermeiroChefeDAO(childBase):
    def __init__(self):
        super().__init__(childModel= EnfermeiroChefe, childSchemaCreated= EnfermeiroChefeCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)