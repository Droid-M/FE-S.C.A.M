class Log_linha:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.dado = values.get("dado")
        self.log_id = values.get("log_id")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
      
    @property
    def foreignKey(self):
         return {"log" : "log_id"}
     
    @property
    def typesAcceptables(self):
         return {
        "id": None,
        'log_id' : None,
        'dado' : None,
        }
     
    @property
    def tableName(self):
         return "log_linha"