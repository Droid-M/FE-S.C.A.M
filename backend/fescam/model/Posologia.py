from fescam.model.Medicamento import Medicamento
from fescam.model.Paciente import Paciente

class Posologia:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.medicamento = values.get("medicamento")
        self.paciente = values.get("paciente")
        self.quantidade = values.get("quantidade")
        self.notas = values.get("notas")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        self.id = values.get("id")
        self.medicamento = values.get("medicamento")
        self.paciente = values.get("paciente")
        self.quantidade = values.get("quantidade")
        self.notas = values.get("notas")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        if(values.get("id") is not None):
            self.id = values.get("id")
        if(values.get("medicamento") is not None):
            self.medicamento = values.get("medicamento")
        if(values.get("paciente") is not None):
            self.paciente = values.get("paciente")
        if(values.get("quantidade") is not None):
            self.quantidade = values.get("quantidade")
        if(values.get("notas") is not None):
            self.notas = values.get("notas")
        if(values.get("created_on") is not None):
            self.created_on = values.get("created_on")
        if(values.get("updated_on") is not None):
            self.updated_on = values.get("updated_on")
    
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
     
    @property
    def foreignKey(self):
        return {
            Medicamento().tableName : "medicamento",
            Paciente().tableName : "paciente",
        }
     
    @property
    def typesAcceptables(self):
        return { #Substituir dicionário por lista no futuro ***
        "id": self.id,
        'medicamento' : self.medicamento,
        "paciente" : self.paciente,
        "quantidade" : self.quantidade,
        "notas" : self.notas,
        "created_on" : self.created_on,
        "updated_on" : self.updated_on,
        }
     
    @property
    def tableName(self):
        return "Posologia"