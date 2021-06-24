from fescam.model.Funcionario import Funcionario

class Estagiario:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.func_id = values.get("func_id")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
      
    @property
    def foreignKey(self):
         return {Funcionario().tableName : "func_id"}
     
    @property
    def typesAcceptables(self):
         return { #Substituir dicionário por lista no futuro ***
        "id": self.id,
        'func_id' : self.func_id,
        }
     
    @property
    def tableName(self):
         return "Estagiario"