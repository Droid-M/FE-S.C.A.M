from fescam.schemas.medicamento import MedicamentoCreated
from fescam.model.Medicamento import Medicamento
from fescam.DAO.base.baseDAO import BaseDAO

class MedicamentoDAO(BaseDAO):
    def __init__(self):
        super().__init__(Medicamento)