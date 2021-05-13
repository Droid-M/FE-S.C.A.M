from app.schemas.funcionario import FuncionarioCreated
from app.model.Funcionario import Funcionario
from app.DAO.base.baseDAO import BaseDAO

class FuncionarioDAO(BaseDAO):
    def __init__(self):
        super().__init__(Funcionario)