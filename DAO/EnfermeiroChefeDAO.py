from schemas.enfermeiroChefe import EnfermeiroChefeCreated
from model.EnfermeiroChefe import EnfermeiroChefe
from model.Funcionario import Funcionario
from DAO.FuncionarioDAO import FuncionarioDAO
from DAO.child.childBase import childBase

class EnfermeiroChefeDAO(childBase):
    def __init__(self):
        super().__init__(childModel= EnfermeiroChefe, childSchemaCreated= EnfermeiroChefeCreated, motherModel= Funcionario, motherDAO= FuncionarioDAO)