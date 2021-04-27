from execute_db_command import execute
#%d/%m/%y %H:%M:%S

class Base(object):
    __tableName = ''
    __typesAlterables = {} #Pode ser modificado indiretamente. Serve como base para os métodos.
    __primaryKey = 'id'
    
    def __init__(self, tableName:str = __tableName, atributes:dict = __typesAlterables, primaryKey = __primaryKey, atributesToSet = {}):
        self.__tableName = tableName
        self.__typesAlterables = atributes
        self.__preSetValues__(atributesToSet)
        self.__primaryKey = primaryKey
    
    def __preSetValues__(self, atributesToSet:dict):
        classAtributes = self.__typesAlterables.copy()
        for atribute in atributesToSet.keys():
            try:
                at = classAtributes[atribute]
            except:
                raise Exception(f"Nome(s) de atributo(s) fornecido(s) inválido(s)! Insira apenas nomes como: {list(self.__typesAlterables.keys())}" )
            classAtributes[atribute] = atributesToSet[atribute]
        self.__typesAlterables = classAtributes #Se der certo, a classe recebe os valores passados

    def __setValue__(self, atribute:str, value):
        try:
            self.__typesAlterables[atribute]
        except:
            raise Exception(f"Não existe o atributo '{atribute}'! Verifique se o método set está correto.")
        self.__typesAlterables[atribute] = value

    def __getValue__(self, atribute:str):
        if(atribute.lower() == "all"):
            return self.__typesAlterables.copy()
        try:
            return self.__typesAlterables[atribute]
        except:
            raise Exception(f"Não existe o atributo '{atribute}'! Verifique se o método get está correto.")