from fescam.DAO.base.baseDAO import BaseDAO
from fescam.schemas.paciente import Dado
from fescam.model.DadoPaciente import DadoPacinte

class DadosPacienteDAO(BaseDAO):
    def __init__(self):
        super().__init__(DadoPacinte)