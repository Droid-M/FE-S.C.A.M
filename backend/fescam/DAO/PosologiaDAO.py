from fescam.DAO.base.baseDAO import BaseDAO
from fescam.schemas.posologia import PosologiaCreated
from fescam.model.Posologia import Posologia

class PosologiaDAO(BaseDAO):
    def __init__(self):
        super().__init__(Posologia)