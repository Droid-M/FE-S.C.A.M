from DAO.base.baseDAO import BaseDAO
from schemas.agendamento import AgendamentoCreated
from model.Agendamento import Agendamento
from DAO.base.baseDAO import BaseDAO

class AgendamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Agendamento)