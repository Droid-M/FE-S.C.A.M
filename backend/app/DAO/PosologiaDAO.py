from backend.app.DAO.base.baseDAO import BaseDAO
from backend.app.schemas.posologia import PosologiaCreated
from backend.app.model.Posologia import Posologia

class PosologiaDAO(BaseDAO):
    def __init__(self):
        super().__init__(Posologia)