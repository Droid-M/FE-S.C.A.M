from app.DAO.base.baseDAO import BaseDAO
from app.schemas.agendamento import AgendamentoCreated
from app.model.Agendamento import Agendamento
from app.DAO.base.baseDAO import BaseDAO

class AgendamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Agendamento)