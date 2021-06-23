from fescam.model.Paciente import Paciente

class DadoPacinte:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.nome_campo = values.get("nome_campo")
        self.valor_campo = values.get("valor_campo")
        self.paciente = values.get("paciente")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
     
    @property
    def foreignKey(self):
         return {Paciente().tableName : "paciente"}
      
    @property
    def typesAcceptables(self):
         return {
          "id": self.id,
          'nome_campo' : self.nome_campo,
          'valor_campo' : self.valor_campo,
          'paciente' : self.paciente
          }
     
    @property
    def tableName(self):
         return "Dado_paciente"