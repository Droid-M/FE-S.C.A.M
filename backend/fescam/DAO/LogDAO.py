from fescam.DAO.base.baseDAO import BaseDAO
from fescam.model.Log import Log

class LogDAO(BaseDAO):
    def __init__(self):
        super().__init__(log)