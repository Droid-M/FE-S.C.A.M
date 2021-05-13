from app.DAO.base.baseDAO import BaseDAO
from app.schemas.posologia import PosologiaCreated
from app.model.Posologia import Posologia

class PosologiaDAO(BaseDAO):
    def __init__(self):
        super().__init__(Posologia)