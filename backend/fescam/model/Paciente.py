class Paciente:
    #Inicializando variaveis para evitar futuros erros (talvez seja desnecessário no futuro) ***:
    
    def __init__(self, **values):
        self.CPF = values.get("CPF")
        self.nome = values.get("nome")
        self.sexo = values.get("sexo")
        self.genero = values.get("genero")
        self.data_nascimento = values.get("data_nascimento")
        self.tipo_sangue = values.get("tipo_sangue")
        self.endereco = values.get("endereco")
        self.telefone = values.get("telefone")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
        self.dados = values.get("dados")
        self.atendente_id = values.get("atendente_id")
    
    def setAll(self, **values): #<-- Sobrescreve todos os valores, até os que não forem passados por parâmetro (recebem None)
        self.CPF = values.get("CPF")
        self.nome = values.get("nome")
        self.sexo = values.get("sexo")
        self.genero = values.get("genero")
        self.data_nascimento = values.get("data_nascimento")
        self.tipo_sangue = values.get("tipo_sangue")
        self.endereco = values.get("endereco")
        self.telefone = values.get("telefone")
        self.created_on = values.get("created_on")
        self.updated_on = values.get("updated_on")
        self.dados = values.get("dados")
        self.atendente_id = values.get("atendente_id")
    
    def updateAll(self, **values): #<-- Apenas sobrescreve os valores que forem passados por parâmetro
        if(values.get("CPF") is not None):
            self.CPF = values.get("CPF")
        if(values.get("nome") is not None):
            self.nome = values.get("nome")
        if(values.get("sexo") is not None):
            self.sexo = values.get("sexo")
        if(values.get("genero") is not None):
            self.genero = values.get("genero")
        if(values.get("data_nascimento") is not None):
            self.data_nascimento = values.get("data_nascimento")
        if(values.get("tipo_sangue") is not None):
            self.tipo_sangue = values.get("tipo_sangue")
        if(values.get("endereco") is not None):
            self.endereco = values.get("endereco")
        if(values.get("telefone") is not None):
            self.telefone = values.get("telefone")
        if(values.get("created_on") is not None):
            self.created_on = values.get("created_on")
        if(values.get("updated_on") is not None):
            self.updated_on = values.get("updated_on")
        if(values.get("dados") is not None):
            self.dados = values.get("dados")
        if(values.get("atendente_id") is not None):
            self.atendente_id = values.get("atendente_id")

    #"Atributos" somente leitura:
    
    @property
    def primaryKey(self):
         return "CPF"
     
    @property
    def typesAcceptables(self):
         return { #Substituir dicionário por lista no futuro ***
        "CPF": self.CPF,
        'nome' : self.nome,
        "sexo" : self.sexo,
        "genero" : self.genero,
        "data_nascimento" : self.data_nascimento,
        "tipo_sangue" : self.tipo_sangue,
        "endereco" : self.endereco,
        "telefone" : self.telefone,
        "created_on" : self.created_on,
        "updated_on" : self.updated_on,
        "dados" : self.dados,
        "atendente_id" : self.atendente_id
        }
     
    @property
    def tableName(self):
         return "Paciente"