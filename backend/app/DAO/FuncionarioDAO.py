from backend.app.schemas.funcionario import FuncionarioCreated
from backend.app.model.Funcionario import Funcionario
from backend.app.DAO.base.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__(Funcionario)