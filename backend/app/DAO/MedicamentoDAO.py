from backend.app.schemas.medicamento import MedicamentoCreated
from backend.app.model.Medicamento import Medicamento
from backend.app.DAO.base.baseDAO import BaseDAO

class MedicamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Medicamento)