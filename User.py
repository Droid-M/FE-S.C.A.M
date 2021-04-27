from Base import Base

class User():
    __typesAlterables = { #Pode ser modificado indiretamente. Serve como base para os métodos.
        'email' : None,
        'password' : None,
        "createdOn" : None,
        "updatedOn" : None
    }
    __tableName = "users"
    __primaryKey = "cpf"
    __base = None

    def __init__(self, **atributesList):
        self.__base = Base(atributes= self.__typesAlterables, tableName= self.__tableName, primaryKey = self.__primaryKey, atributesToSet = atributesList)
        
    #Setters:
    def setEmail(self, value):
        self.__base.__setValue__("email", value)
        
    def setPassword(self, value):
        self.__base.__setValue__("password", value)
        
    def setAll(self, dictValues:dict):
        self.__base.__preSetValues__(dictValues)
    
    #Getters:
    def getEmail(self):
        return self.__base.__getValue__("email")

    def getPassword(self):
        return self.__base.__getValue__("password")

    def getCreatedOn(self):
        return self.__base.__getValue__("created_on")

    def getTypeUpdatedOn(self):
        return self.__base.__getValue__("updated_on")
    
    def getAll(self):
        return self.__base.__getValue__("all")