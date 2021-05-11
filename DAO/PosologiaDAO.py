from DAO.base.baseDAO import BaseDAO
from schemas.posologia import PosologiaCreated
from model.Posologia import Posologia

class PosologiaDAO(BaseDAO):
    def __init__(self):
        super().__init__(Posologia)