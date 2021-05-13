from backend.app.DAO.DAO_SQL_M.DAO_TO_SQL import DAO_TO_SQL
from backend.app.model.IBaseModel import IBase

class childBase:
    
    def __init__(self, childModel, childSchemaCreated, motherModel, motherDAO):
        #self.__childSchemaCreated = childSchemaCreated
        self.__parentDAO = motherDAO()
        self.__parent = motherModel()
        self.__child = childModel()
        self.__base = DAO_TO_SQL(tableName = self.__child.tableName, atributes = self.__child.typesAcceptables, schemaBase = motherModel)
        #self.__motherModel = motherModel
    
    #Retornam esquema(s):
    
    def createByTuple(self, **attAndValues): #Considerando que o retorno vai ser uma instância de schema ou do model ou None:
        result = self.__parentDAO.createByTuple(**attAndValues)
        if(result is not None):
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            valueFK = attAndValues.get(self.__parent.primaryKey)
            self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod = False)
        return result
    
    def createBySchema(self, instanceData):
        result = self.__parentDAO.createBySchema(instanceData)
        if(result is not None):
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            valueFK = instanceData.dict()[self.__parent.primaryKey]
            self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod = False)
        return result
    
    def store(self, instanceData) -> bool:
        if(self.__parentDAO.store(instanceData)):
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            valueFK = instanceData.typesAcceptables[instanceData.primaryKey]
            result = self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod= False) #Considerando que o retorno vai ser um dicionário:
            return True if (result is not None) and len(result) > 0 else False
        return False
        
    def findByPK(self, primaryKeyValue):
        #primaryKeyValue = ForeignKey aqui **
        #Essa classe:
        foreignKey = self.__child.foreignKey[self.__parent.tableName]
        tableName = self.__child.tableName
        TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
        #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
        parentTableName = self.__parent.tableName
        parentPK = self.__parent.primaryKey
        PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
        return self.__base._find(atributes = list(self.__parent.typesAcceptables.keys()), convertMethod= True, toJoin = {
            "tableName":parentTableName,
            "foreignKey":parentPK #<--Tá correto, a PK desta classe é a FK de outra
        }).ON(TN_period_FK, "=", f"'{primaryKeyValue}'").AND(TN_period_FK, "=", PTN_period_PPK).getFirst()
    
    def DeleteByPK(self, primaryKeyValue): #Possivelmente vai ser inutilizado kk
        #primaryKeyValue = ForeignKey aqui **
        #Essa classe:
        foreignKey = self.__child.foreignKey[self.__parent.tableName]
        tableName = self.__child.tableName
        TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
        #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
        parentTableName = self.__parent.tableName
        parentPK = self.__parent.primaryKey
        PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
        return  self.__base._remove(convertMethod= True, toUse= {
            "tableName" : parentTableName,
            "atributesToReturn": list(self.__parent.typesAcceptables.keys())
        }).WHERE(TN_period_FK, "=", PTN_period_PPK).AND(TN_period_FK, "=", f"'{primaryKeyValue}'").getFirst()
    
    def getAll(self):
        #primaryKeyValue = ForeignKey aqui **
        #Essa classe:
        foreignKey = self.__child.foreignKey[self.__parent.tableName]
        tableName = self.__child.tableName
        TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
        #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
        parentTableName = self.__parent.tableName
        parentPK = self.__parent.primaryKey
        PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
        return self.__base._find(atributes = list(self.__parent.typesAcceptables.keys()), convertMethod= True, toJoin = {
            "tableName":parentTableName,
            "foreignKey":parentPK
        }).ON(TN_period_FK, "=", PTN_period_PPK).getAll()
    
    def refresh(self, instanceData): #<-- A chave primária não pode ser nula (None)
        self.__parentDAO.refresh(instanceData)
        
    def update(self, instanceData): #Preciso fazer update com Join?**************
        instancePKValue = instanceData.typesAcceptables[instanceData.primaryKey]
        result = self.findByPK(instancePKValue)
        if(result is not None):
            #primaryKeyValue = ForeignKey aqui **
            
            #Essa classe:
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            tableName = self.__child.tableName
            TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
            result_valuePK = result.typesAcceptables[result.primaryKey]
            #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
            parentTableName = self.__parent.tableName
            parentPK = self.__parent.primaryKey
            PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
            result = self.__base._save(instanceData.typesAcceptables, toInsert= False, toJoinOnUpdate = instanceData.tableName).FROM(
                self.__child.tableName).WHERE(
                    TN_period_FK, "=", PTN_period_PPK).AND(TN_period_FK, "=", f"'{result_valuePK}'").getFirst()
            return (result is not None)
        return False
        #return self.__parentDAO.update(instanceData)
    
    
    #Retornam dicionário(s) por padrão:
    
    def SELECT(self, atributes:list, convertReturn = False):
        return self.__parentDAO.SELECT(atributes = atributes, convertReturn = convertReturn)
    
    def INSERT(self, atributeEValue:dict, convertReturn = False):
        return self.__parentDAO.INSERT(atributeEValue= atributeEValue, convertReturn= convertReturn)
    
    def UPDATE(self, atributeEValue:dict, convertReturn = False):
        return self.__parentDAO.UPDATE(atributeEValue = atributeEValue, convertReturn= convertReturn)
    
    def DELETE(self, convertReturn = False):
        return self.__parentDAO.DELETE(convertReturn= convertReturn)