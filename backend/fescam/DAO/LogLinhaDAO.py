from fescam.DAO.base.baseDAO import BaseDAO
from fescam.model.log_linha import Log_linha

class LogLinhaDAO(BaseDAO):
    def __init__(self):
        super().__init__(Log_linha)