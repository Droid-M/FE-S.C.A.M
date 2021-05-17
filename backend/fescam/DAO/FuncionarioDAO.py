from os import path
import sys

sys.path.append(path.abspath('.'))
from fescam.schemas.funcionario import FuncionarioCreated
from fescam.model.Funcionario import Funcionario
from fescam.DAO.base.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__(Funcionario)