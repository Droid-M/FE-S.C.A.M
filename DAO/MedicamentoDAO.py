from schemas.medicamento import MedicamentoCreated
from model.Medicamento import Medicamento
from DAO.base.baseDAO import BaseDAO

class MedicamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Medicamento)