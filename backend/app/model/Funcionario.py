class Funcionario:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.CPF = values.get("CPF")
        self.nome = values.get("nome")
        self.senha = values.get("senha")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        self.CPF = values.get("CPF")
        self.nome = values.get("nome")
        self.senha = values.get("senha")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        if(values.get("CPF") is not None):
            self.CPF = values.get("CPF")
        if(values.get("nome") is not None):
            self.nome = values.get("nome")
        if(values.get("senha") is not None):
            self.senha = values.get("senha")
        if(values.get("created_on") is not None):
            self.created_on = values.get("created_on")
        if(values.get("updated_on") is not None):
            self.updated_on = values.get("updated_on")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
        return "CPF"
     
    @property
    def typesAcceptables(self):
        return { #Substituir dicionário por lista no futuro ***
        "CPF": self.CPF,
        'nome' : self.nome,
        "senha" : self.senha,
        "created_on" : self.created_on,
        "updated_on" : self.updated_on,
        }
     
    @property
    def tableName(self):
        return "Funcionario"