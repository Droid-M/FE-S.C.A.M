from backend.app.DAO.base.baseDAO import BaseDAO
from backend.app.schemas.agendamento import AgendamentoCreated
from backend.app.model.Agendamento import Agendamento
from backend.app.DAO.base.baseDAO import BaseDAO

class AgendamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Agendamento)