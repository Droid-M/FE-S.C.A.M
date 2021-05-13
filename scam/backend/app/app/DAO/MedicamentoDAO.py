from app.schemas.medicamento import MedicamentoCreated
from app.model.Medicamento import Medicamento
from app.DAO.base.baseDAO import BaseDAO

class MedicamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Medicamento)