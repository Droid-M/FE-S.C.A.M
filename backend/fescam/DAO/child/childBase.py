from fescam.DAO.DAO_SQL_M.DAO_TO_SQL import DAO_TO_SQL
from fescam.model.IBaseModel import IBase

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
            if(self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod = False) is None):
                self.__parentDAO.deleteByTuple(**attAndValues)
                return None
        return result
    
    def createBySchema(self, instanceData):
        result = self.__parentDAO.createBySchema(instanceData)
        if(result is not None):
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            valueFK = instanceData.dict()[self.__parent.primaryKey]
            if(self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod = False) is None):
                self.__parentDAO.deleteByTuple(**instanceData.dict())
                return None
        return result
    
    def store(self, instanceData) -> bool:
        if(self.__parentDAO.store(instanceData)):
            foreignKey = self.__child.foreignKey[self.__parent.tableName]
            valueFK = instanceData.typesAcceptables[instanceData.primaryKey]
            result = self.__base._save(atributeEValue = {foreignKey:valueFK}, convertMethod= False) #Considerando que o retorno vai ser um dicionário:
            return True if (result is not None) and len(result) > 0 else False
        return False
        
    def findByFK(self, primaryKeyValue, convert = True):
        #primaryKeyValue = ForeignKey aqui **
        #Essa classe:
        foreignKey = self.__child.foreignKey[self.__parent.tableName]
        tableName = self.__child.tableName
        TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
        #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
        parentTableName = self.__parent.tableName
        parentPK = self.__parent.primaryKey
        PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
        return self.__base._find(atributes = list(self.__parent.typesAcceptables.keys()), convertMethod= convert, toJoin = {
            "tableName":parentTableName,
            "foreignKey":parentPK #<--Tá correto, a PK desta classe é a FK de outra
        }).ON(TN_period_FK, "=", f"'{primaryKeyValue}'").AND(TN_period_FK, "=", PTN_period_PPK).getFirst()
    
    def DeleteByFK(self, primaryKeyValue): #Possivelmente vai ser inutilizado kk
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
    
    def getAll(self, convert = True, disassociate = False):
        if(disassociate):
            return self.__base._find(atributes = list(self.__child.typesAcceptables.keys()), convertMethod = convert, getAllTuples = True).getAll()
        #primaryKeyValue = ForeignKey aqui **
        #Essa classe:
        foreignKey = self.__child.foreignKey[self.__parent.tableName]
        tableName = self.__child.tableName
        TN_period_FK = tableName + "." + foreignKey #tn = tableName; period = .; fk = foreignKey
        #Classe pai/mãe/avô/tio/sei lá, pode até ser adotada:
        parentTableName = self.__parent.tableName
        parentPK = self.__parent.primaryKey
        PTN_period_PPK = parentTableName+ "." + parentPK #ptn= parentTableName; PPK = parentPK
        return self.__base._find(atributes = list(self.__parent.typesAcceptables.keys()), convertMethod= convert, toJoin = {
            "tableName":parentTableName,
            "foreignKey":parentPK
        }).ON(TN_period_FK, "=", PTN_period_PPK).getAll()
    
    def refresh(self, instanceData): #<-- A chave primária não pode ser nula (None)
        self.__parentDAO.refresh(instanceData)
        
    def update(self, instanceData): #Preciso fazer update com Join?**************
        instancePKValue = None
        dictValuesToUpd = None
        if(type(instanceData) == type(self.__parent)):
            dictValuesToUpd = instanceData.typesAcceptables
            dictValuesToUpd.pop('updated_on') #<-- tirando esse dado pois o DAO_TO_SQL se encarrega de preencher a informação
        else:
            try:
                dictValuesToUpd = instanceData.dict() #Supondo que a instância é filiada de pydantic.baseModel
                dictValuesToUpd.pop('updated_on') #<-- tirando esse dado pois o DAO_TO_SQL se encarrega de preencher a informação
            except(Exception):
                print(Exception)
        
        if(dictValuesToUpd is None or type(dictValuesToUpd) != dict):
            return None
        
        instancePKValue = dictValuesToUpd[self.__parent.primaryKey]
        result = self.findByFK(instancePKValue)
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
            result = self.__base._save(dictValuesToUpd, toInsert= False, toJoinOnUpdate = self.__parent.tableName, convertMethod= True).FROM(
                self.__child.tableName).WHERE(
                    TN_period_FK, "=", PTN_period_PPK).AND(TN_period_FK, "=", f"'{result_valuePK}'").getFirst()
        return result
        #return self.__parentDAO.update(instanceData)
    
    
    #Retornam dicionário(s) por padrão:
    
    def SELECT(self, atributes:list, disassociate = False, convertReturn = False):
        if(disassociate):
            return self.__base._find(atributes = atributes, convertMethod= convertReturn)
        return self.__base._find(atributes = atributes, convertMethod= convertReturn, toJoin = {
            "tableName":self.__parent.tableName,
            "foreignKey":self.__parent.primaryKey
        })
    
    def INSERT(self, atributeEValue:dict, convertReturn = False):
        return self.__parentDAO.INSERT(atributeEValue= atributeEValue, convertReturn= convertReturn)
    
    def UPDATE(self, atributeEValue:dict, convertReturn = False):
        return self.__parentDAO.UPDATE(atributeEValue = atributeEValue, convertReturn= convertReturn)
    
    def DELETE(self, convertReturn = False):
        return self.__parentDAO.DELETE(convertReturn= convertReturn)