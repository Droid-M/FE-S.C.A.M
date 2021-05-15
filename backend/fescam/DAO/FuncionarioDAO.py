from os import path
import sys

sys.path.append(path.abspath('.'))
from backend.fescam.schemas.funcionario import FuncionarioCreated
from backend.fescam.model.Funcionario import Funcionario
from backend.fescam.DAO.base.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__(Funcionario)