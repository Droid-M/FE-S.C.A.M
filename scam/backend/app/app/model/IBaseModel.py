class IBase:
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        return
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        return
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
        return
     
    @property
    def typesAcceptables(self):
        return
     
    @property
    def tableName(self):
        return