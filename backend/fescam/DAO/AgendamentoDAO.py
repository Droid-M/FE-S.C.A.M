from fescam.DAO.base.baseDAO import BaseDAO
from fescam.schemas.agendamento import AgendamentoCreated
from fescam.model.Agendamento import Agendamento
from fescam.DAO.base.baseDAO import BaseDAO

class AgendamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Agendamento)