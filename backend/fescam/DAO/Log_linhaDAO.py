from fescam.DAO.base.baseDAO import BaseDAO
from fescam.model.log_linha import Log_linha
from fescam.DAO.base.baseDAO import BaseDAO

class AgendamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Log_linha)