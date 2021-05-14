class Medicamento:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.codigo = values.get("codigo")
        self.nome = values.get("nome")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        self.codigo = values.get("codigo")
        self.nome = values.get("nome")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        if(values.get("codigo") is not None):
            self.codigo = values.get("codigo")
        if(values.get("nome") is not None):
            self.nome = values.get("nome")
        if(values.get("created_on") is not None):
            self.created_on = values.get("created_on")
        if(values.get("updated_on") is not None):
            self.updated_on = values.get("updated_on")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
        return "codigo"
     
    @property
    def typesAcceptables(self):
        return { #Substituir dicionário por lista no futuro ***
        "codigo": self.codigo,
        'nome' : self.nome,
        "created_on" : self.created_on,
        "updated_on" : self.updated_on,
        }
     
    @property
    def tableName(self):
        return "Medicamento"