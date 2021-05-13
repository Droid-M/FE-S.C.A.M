from app.DAO.base.baseDAO import BaseDAO
from app.schemas.paciente import PacienteCreated
from app.model.Paciente import Paciente

class PacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__(Paciente)