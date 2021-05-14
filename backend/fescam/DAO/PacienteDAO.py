from fescam.DAO.base.baseDAO import BaseDAO
from fescam.schemas.paciente import PacienteCreated
from fescam.model.Paciente import Paciente

class PacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__(Paciente)