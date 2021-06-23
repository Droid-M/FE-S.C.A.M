class Log:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
      
    @property
    def typesAcceptables(self):
         return { #Substituir dicionário por lista no futuro ***
        "id": None,
        'created_on' : None,
        'updated_on' : None
        }
     
    @property
    def tableName(self):
         return "Log"