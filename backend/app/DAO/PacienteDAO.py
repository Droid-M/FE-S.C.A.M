from backend.app.DAO.base.baseDAO import BaseDAO
from backend.app.schemas.paciente import PacienteCreated
from backend.app.model.Paciente import Paciente

class PacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__(Paciente)