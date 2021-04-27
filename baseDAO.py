from execute_db_command import execute
from db_helpers import create_list_dicitionary
from RaiseException import ErrorMessage

class baseDAO:
    __typesAcceptables = {} #Serve como base para os métodos. O usuário não modifica diretamente
    __tableName = ''
    __cheating = True #Não se trata de um jogo. Isso é só pra saber se a ordem de chamada dos métodos foi burlada
    
    def __init__(self, tableName:str = __tableName, atributes:dict = __typesAcceptables):
        self.__tableName = tableName
        self.__typesAcceptables = atributes
    
    class __storageCommand:
        __cheating = True #Não se trata de um jogo. Isso é só pra saber se a ordem de chamada dos métodos foi burlada
        __typesAcceptables = [
            
        ]
        __commandToDB = ''
        def __init__(self, command:str = None, typesAcceptables:list = None):
            self.__typesAcceptables = typesAcceptables
            self.__commandToDB = command
        
        def _convertCommand(self, tupleValues):
            count = 0
            command = ''
            length = len(tupleValues)
            #Validando o número de posições:
            copyLength = length
            while(copyLength > -1):
                copyLength -= 4
            if(copyLength != -1):
                raise ValueError("Quantidade de parâmetros inválida! Insira na ordem, respeitando a quantidade conforme o exemplo: (name, '=', 'Son Goku', 'OR', 'KI', '>', '8000').") #Vegeta, é mais 8 mil!
            
            for i in range(0, length - 1, 1):
                if(count == 3): #conectores AND e NOT
                    if (str(tupleValues[i]).lower() != 'and' and str(tupleValues[i]).lower() != 'or'):
                        raise ValueError(f"Paramêtro incorreto na posição {i + 1}! Tipo AND ou OR esperado.")
                    command += tupleValues[i] + ' '
                    count = -1
                elif(count == 2): #valor
                    command += f"'{tupleValues[i]}' " if(tupleValues[i] is not None) else 'NULL '
                elif(count == 1): #Sinal de comparação
                    if(tupleValues[i] != '=' and tupleValues[i] != '>' and tupleValues[i] != '>=' and tupleValues[i] != '<' and tupleValues[i] != '<=' and tupleValues[i] != '!='):
                        raise ValueError(f"Sinal incorreto na posição {i + 1}! Comparador '=', '>', '>=', '<', '<=' ou '!=' esperado.")
                    command += tupleValues[i] + ' '
                elif(count == 0): #Nome do atributo
                    paramIsOk = False
                    msg = ''
                    for p in self.__typesAcceptables:
                        msg += p + ', '
                        if(p == tupleValues[i]): #<- Na posição referente ao campo atributo
                            paramIsOk = True
                    if(not paramIsOk):
                        raise ValueError(f"Paramêtro incorreto na posição {i + 1}! Nomes de atributo {msg} esperados.")
                    command += tupleValues[i] + ' '
                count += 1
            #Adicionando ultimo item (valor):
            if(length > 0):
                command += f"'{tupleValues[length - 1]}'" if(tupleValues[length - 1] is not None) else 'NULL'
            return command

        def AND(self, *values):
                if (len(values) == 0):
                    raise ValueError("Impossível impor uma condição secundária sem uma primária definida. Informe as condições primárias usando o método WHERE.")
                self.__commandToDB += f" AND ({self._convertCommand(values)})"
                return self

        def OR(self, *values):
            if (len(values) == 0):
                raise ValueError("Impossível impor uma condição secundária sem uma primária definida. Informe as condições primárias usando o método WHERE.")
            self.__commandToDB += f" OR ({self._convertCommand(values)})"
            return self
            
        def _extractCommand(self):
            return self.__commandToDB
    
    def _lstrListToStr(self, list, separator:str) -> str:
        result = ''
        for item in list:
            assert(type(separator) == str)
            result += item + separator
        return result[:-1]

    def _WHERE(self, values):
        commandToDB = ''
        if len(values) == 0:
            raise ValueError("Impossível impor uma condição sem atributos, comparadores e valores definidos.")
        commandToDB += f"WHERE ({self.__storageCommand(command = commandToDB, typesAcceptables = list(self.__typesAcceptables.keys()))._convertCommand(values)})"
        nextCommand = self.__storageCommand(command = commandToDB, typesAcceptables = list(self.__typesAcceptables.keys()))
        self.__cheating = False
        return nextCommand

    def _find(self, atributes:list, condition:__storageCommand):
        commandToDB = ''
        try:
            commandToDB = condition._extractCommand()
        except(Exception):
            print("Passagem inválida! Para extrair informações use o método 'WHERE'")
            
        if (commandToDB == '' or commandToDB is None) or (self.__cheating):
            raise ValueError("Impossível realizar objetivo sem uma condição imposta. Informe as condições necessárias usando o método WHERE.") #msg for life kk
        atributesToSave = ''
        if(len(atributes) == 0):
            return [{}]
        for atribute in atributes:
            try:
                self.__typesAcceptables[atribute]
            except:
                raise ValueError(f"Nome(s) de atributo(s) fornecido(s) inválido(s)! Insira apenas nomes como: {list(self.__typesAcceptables.keys())}" )
            if(type(atribute) is not str):
                raise ValueError(f"Paramêtro incorreto na posição {i + 1}! É necessário que o parâmetro seja do tipo String (str).")
            else:
                atributesToSave += atribute + ','
        atributesToSave = atributesToSave[:-1] #Remove a ultima vírgula pra evitar erros futuros
        commandToDB = f"SELECT {atributesToSave} from {self.__tableName} {commandToDB}"
        self.__cheating = True
        return create_list_dicitionary(atributesToSave.split(','), execute(commandToDB))
        
    def _save(self, atributeEValue:dict, condition:__storageCommand = None, toInsert = True): #Tratar atributos inexistentes depois ********
        if (self.__cheating and toInsert == False):
            raise ValueError("Chamada de método em local indevido! Faça conforme o exemplo: [object_name].[method_name]()")
        commandToDB = ''
        atributesLength = len(atributeEValue)
        count = 0
        atributesToSave = '' #atributo, atributo
        valuesToSave = '' #'valor', 'valor'
        AtributesEvaluesToUpdate = '' #atributo = 'valor'
        for atribute, value in atributeEValue.items():
            count += 1
            if(count == atributesLength):
                atributesToSave += atribute
                valuesToSave += f"'{value}'"
                AtributesEvaluesToUpdate += f"{atribute} = '{value}'"
            else:
                atributesToSave += atribute + ','
                valuesToSave += f"'{value}',"
                AtributesEvaluesToUpdate += f"{atribute} = '{value}',"
        toReturn = self._lstrListToStr(list(self.__typesAcceptables.keys()), ",")
        if(toInsert == True): #Se o objeto ainda não está no banco
            commandToDB = f"INSERT INTO {self.__tableName}({atributesToSave}) VALUES ({valuesToSave}) RETURNING {toReturn}"
        elif(condition == None):
            return [{}]
        else:
            try:
                condition = condition._extractCommand()
            except(Exception):
                print("Passagem inválida! Para extrair informações use o método 'WHERE'")
            AtributesEvaluesToUpdate += ',updated_on = NOW()'
            commandToDB = f"UPDATE {self.__tableName} SET {AtributesEvaluesToUpdate} {condition} RETURNING {toReturn}"
        return create_list_dicitionary(list(self.__typesAcceptables.keys()), execute(commandToDB))
    
    def _remove(self, condition:__storageCommand):
        commandToDB = ''
        try:
            commandToDB = condition._extractCommand()
        except(Exception):
            print("Passagem inválida! Para extrair informações use o método 'WHERE'")
        toReturn = self._lstrListToStr(list(self.__typesAcceptables.keys()), ",")
        commandToDB = f"DELETE FROM {self.__tableName} {commandToDB} RETURNING {toReturn}"
        return create_list_dicitionary(list(self.__typesAcceptables.keys()), execute(commandToDB))
    
    def _findByKey(self, keyName, keyValue):
        try:
            self.__typesAcceptables[keyName]
        except:
            raise ValueError(f"Nome(s) de atributo(s) fornecido(s) inválido(s)! Insira apenas nomes como: {list(self.__typesAcceptables.keys())}" )
        param = keyName, "=", keyValue
        return self._find(list(self.__typesAcceptables.keys()), self._WHERE(param))