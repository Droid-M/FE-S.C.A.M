#Talvez eu não use ****
class ErrorMessage(Exception):
    __msgError = "Algo de errado não está certo..."
    def __init__(self, msg = __msgError):
        self.__msgError = msg
    def __str__(self):
        return self.__msgError