from baseDAO import baseDAO
from User import User

class UserDAO():
    __typesAcceptables = { #Serve como base para os métodos. O usuário não modifica diretamente
        'email' : None,
        'password' : None,
        "createdOn" : None,
        "updatedOn" : None
    }
    __tableName = "users"
    __base = baseDAO(tableName = __tableName, atributes = __typesAcceptables)
    
    def findUserByEmail(self, value):
        result = self.__base._findByKey("email", value)
        if(len(result) > 0):
            user = User()
            user.setAll(result[0])
            return user
        return None
    
    def findUsers(self, condition):
        results = self.__base._find(atributes = list(self.__typesAcceptables.keys()), condition = condition)
        users = []
        for result in results:
            newUser = User()
            newUser.setAll(result)
            users.append(newUser)
        return users
    
    #Comandos comuns
    
    def SELECT(self, atributes:list, condition):
        return self.__base._find(atributes = atributes, condition = condition)
    
    def WHERE(self, *values):
        return self.__base._WHERE(values)
    
    def INSERT(self, atributeEValue:dict):
        return self.__base._save(atributeEValue = atributeEValue)
    
    def UPDATE(self, atributeEValue:dict, condition):
        return self.__base._save(atributeEValue = atributeEValue, toInsert = False, condition = condition)
    
    def DELETE(self, condition):
        return self.__base._remove(condition)