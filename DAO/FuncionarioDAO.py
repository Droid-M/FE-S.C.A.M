from schemas.funcionario import FuncionarioCreated
from model.Funcionario import Funcionario
from DAO.base.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__(Funcionario)