from DAO.base.baseDAO import BaseDAO
from schemas.paciente import PacienteCreated
from model.Paciente import Paciente

class PacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__(Paciente)