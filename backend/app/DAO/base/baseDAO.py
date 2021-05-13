from app.DAO.DAO_SQL_M.DAO_TO_SQL import DAO_TO_SQL
from app.components.functions_helpers import dictToSQLConditions
#from model.childModel import childModel

class BaseDAO:
    def __init__(self, classModel): # classes que podem ser usadas futuramente: classSchemaCreated, classDAO
        self.__classModel = classModel()
        self.__primaryKey = self.__classModel.primaryKey
        self.__typesAcceptables = self.__classModel.typesAcceptables
        self.__tableName = self.__classModel.tableName
        self.__base = DAO_TO_SQL(tableName = self.__tableName, atributes = self.__typesAcceptables, schemaBase = classModel)
    
    #Retornam esquema(s):
    
    def createByTuple(self, **attAndValues): #Considerando que o retorno vai ser uma instância de schema ou do model ou None:
        return self.__base._save(atributeEValue = attAndValues, convertMethod= True)
    
    def createBySchema(self, instanceData):
        return self.__base._save(atributeEValue = instanceData.dict(), convertMethod= True) #Considerando que o retorno vai ser um dicionário:
    
    def store(self, instanceData):
        result = self.__base._save(atributeEValue = instanceData.typesAcceptables, convertMethod= False) #Considerando que o retorno vai ser um dicionário:
        return True if (result is not None) and len(result) > 0 else False
        
    def findByPK(self, primaryKeyValue):
        return self.__base._find(atributes = list(self.__typesAcceptables.keys()), convertMethod= True).WHERE(self.__primaryKey, "=", primaryKeyValue).getFirst()
    
    def findByTuple(self, **attAndValues):
        return self.__base._find(atributes = list(self.__typesAcceptables.keys()), convertMethod= True).WHERE(dictToSQLConditions(attAndValues)).getAll()
    
    def DeleteByPK(self, primaryKeyValue): #Possivelmente vai ser inutilizado kk
        return self.__base._remove(convertMethod= True).WHERE(self.__primaryKey, "=", primaryKeyValue).getFirst()
    
    def deleteByTuple(self, **attAndValues):
        return self.__base._remove(convertMethod= True).WHERE(dictToSQLConditions(attAndValues)).getAll()
    
    def getAll(self):
        return self.__base._find(atributes = list(self.__typesAcceptables.keys()), convertMethod = True, getAllTuples = True).getAll()
    
    def refresh(self, instanceData): #<-- A chave primária não pode ser nula (None)
        pkValue = instanceData.typesAcceptables[instanceData.primaryKey]
        result = self.__base._find(atributes = list(self.__typesAcceptables.keys()), convertMethod= True).WHERE(self.__primaryKey, "=", pkValue).getFirst()
        if(result is not None):
            instanceData.setAll(**result.typesAcceptables)
            
    def update(self, instanceData):
        instancePKValue = instanceData.typesAcceptables[instanceData.primaryKey]
        result = self.findByPK(instancePKValue)
        if(result is None):
            return False
        resultPKValue = result.typesAcceptables[result.primaryKey]
        resultTypes = instanceData.typesAcceptables
        resultTypes.pop('updated_on')
        result = self.__base._save(atributeEValue = resultTypes, convertMethod= False, toInsert= False).WHERE(self.__primaryKey, "=", resultPKValue).getFirst() #Considerando que o retorno vai ser um dicionário:
        return True if (result is not None) and len(result) > 0 else False
    
    #Retornam dicionário(s) por padrão:
    
    def SELECT(self, atributes:list, convertReturn = False):
        return self.__base._find(atributes = atributes, convertMethod= convertReturn)
    
    def INSERT(self, atributeEValue:dict, convertReturn = False):
        return self.__base._save(atributeEValue = atributeEValue, convertMethod= convertReturn)
    
    def UPDATE(self, atributeEValue:dict, convertReturn = False):
        return self.__base._save(atributeEValue = atributeEValue, toInsert = False, convertMethod= convertReturn)
    
    def DELETE(self, convertReturn = False):
        return self.__base._remove(convertMethod= convertReturn)