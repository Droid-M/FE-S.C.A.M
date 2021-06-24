from fescam.model.Medicamento import Medicamento
from fescam.model.Paciente import Paciente
from fescam.model.EnfermeiroChefe import EnfermeiroChefe
from fescam.model.Enfermeiro import Enfermeiro
from fescam.model.Estagiario import Estagiario
from fescam.model.Posologia import Posologia

class Agendamento:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.id = values.get("id")
        self.posologia = values.get("posologia")
        self.paciente = values.get("paciente")
        self.enfermeiro = values.get("enfermeiro")
        self.estagiario = values.get("estagiario")
        self.enferchefe = values.get("enferchefe")
        self.horario = values.get("horario")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        self.id = values.get("id")
        self.posologia = values.get("posologia")
        self.paciente = values.get("paciente")
        self.enfermeiro = values.get("enfermeiro")
        self.estagiario = values.get("estagiario")
        self.enferchefe = values.get("enferchefe")
        self.horario = values.get("horario")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        if(values.get("id") is not None):
            self.id = values.get("id")
        if(values.get("posologia") is not None):
            self.posologia = values.get("posologia")
        if(values.get("paciente") is not None):
            self.paciente = values.get("paciente")
        if(values.get("enfermeiro") is not None):
            self.enfermeiro = values.get("enfermeiro")
        if(values.get("estagiario") is not None):
            self.estagiario = values.get("estagiario")
        if(values.get("horario") is not None):
            self.horario = values.get("horario")
        if(values.get("created_on") is not None):
            self.created_on = values.get("created_on")
        if(values.get("updated_on") is not None):
            self.updated_on = values.get("updated_on")
        if(values.get("enferchefe") is not None):
            self.enferchefe = values.get("enferchefe")
        
    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "id"
    
    @property
    def foreignKey(self):
        return {
            Posologia().tableName : "posologia",
            Paciente().tableName : "paciente",
            Enfermeiro().tableName : "enfermeiro",
            Estagiario().tableName : "estagiario",
            EnfermeiroChefe().tableName : "enferchefe",
        }
         
    @property
    def typesAcceptables(self):
         return { #Substituir dicionário por lista no futuro ***
        "id": self.id,
        'posologia' : self.posologia,
        "paciente" : self.paciente,
        "enfermeiro" : self.enfermeiro,
        "estagiario" : self.estagiario,
        "enferchefe" : self.enferchefe,
        "created_on" : self.created_on,
        "updated_on" : self.updated_on,
        "horario": self.horario
        }
     
    @property
    def tableName(self):
         return "Agendamento"