from fescam.components.functions_helpers import create_list_dicitionary, create_dictionary
from fescam.db.execute_db_command import execute

#EXTRAIR A CLASSE CONVERT_COMAND E A CLASSE WHERE NO FUTURO *************************

#Trocar list() por []? *****
class DAO_TO_SQL: #Adicionar uma variável representando todos os toReturn convertidos em string ***************
    def __init__(self, tableName:str, atributes:dict, schemaBase = None):
        self.__tableName = tableName
        self.__typesAcceptables = atributes
        self.__schemaBase = schemaBase
        self._aspas = "'"
    
    def _lstrListToStr(self, list, separator:str):
        result = ''
        for item in list:
            assert(type(separator) == str)
            result += item + separator
        return result[:-1]

    def _convertToSchema(self, schemaData):
        if(type(schemaData) == list): #Provavelmente uma lista de dicionários
            schemaList = []    
            for d in schemaData:
                schemaList.append(self._convertToSchema(d))
            return schemaList
        else: #Provavelmente um objeto dicionário
            if(len(schemaData) > 0) and (self.__schemaBase != None):
                return self.__schemaBase(**schemaData)
            return None
    
    def _convertCommand(self, tupletablesNames):
            count = 0
            command = ''
            length = len(tupletablesNames)
            #Validando o número de posições:
            copyLength = length
            while(copyLength > -1):
                copyLength -= 4
            if(copyLength != -1):
                raise ValueError("Quantidade de parâmetros inválida! Insira na ordem, respeitando a quantidade conforme o exemplo: (name, '=', 'Son Goku', 'OR', 'KI', '>', '8000').") #Vegeta, é mais 8 mil!
            
            for i in range(0, length - 1, 1):
                if(count == 3): #conectores AND e NOT
                    if (str(tupletablesNames[i]).lower() != 'and' and str(tupletablesNames[i]).lower() != 'or'):
                        raise ValueError(f"Paramêtro incorreto na posição {i + 1}! Tipo AND ou OR esperado.")
                    command += tupletablesNames[i] + ' '
                    count = -1
                elif(count == 2): #valor
                    command += f"{self._aspas + str(tupletablesNames[i]) + self._aspas} " if(tupletablesNames[i] is not None) else 'NULL '
                elif(count == 1): #Sinal de comparação
                    if(tupletablesNames[i] != '=' and tupletablesNames[i] != '>' and tupletablesNames[i] != '>=' and tupletablesNames[i] != '<' and tupletablesNames[i] != '<=' and tupletablesNames[i] != '!='):
                        raise ValueError(f"Sinal incorreto na posição {i + 1}! Comparador '=', '>', '>=', '<', '<=' ou '!=' esperado.")
                    command += tupletablesNames[i] + ' '
                elif(count == 0): #Nome do atributo
                    command += tupletablesNames[i] + ' '
                count += 1
            #Adicionando ultimo item (valor):
            if(length > 0):
                command += f"{self._aspas + str(tupletablesNames[length - 1]) + self._aspas}" if(tupletablesNames[length - 1] is not None) else 'NULL'
            return command
    
    class _executeCommand:
        def __init__(self, command:str, atributes, convertMethod, returning = ''):
            self.__commandToDB = command
            self.__convertMethod = convertMethod
            self.__returning = returning
            self.__atributes = atributes
        
        def getFirst(self):
            if(self.__convertMethod is None): #Se não houver forma de conversão, retorne um dicionário
                return create_dictionary(self.__atributes, execute(self.__commandToDB + self.__returning))
            return self.__convertMethod(create_dictionary(self.__atributes, execute(self.__commandToDB + self.__returning)))
        
        def getAll(self):
            if(self.__convertMethod is None): #Se não houver forma de conversão, retorne um dicionário
                return create_list_dicitionary(self.__atributes, execute(self.__commandToDB + self.__returning, getAll= True))
            return self.__convertMethod(create_list_dicitionary(self.__atributes, execute(self.__commandToDB + self.__returning, getAll= True)))
    
    class __storageCommand():
        __commandToDB = ''
        
        def __init__(self, command:str, convertCommand, atributes, convertMethod, returning, executeCommand):
            self.__commandToDB = command
            self.__convertCommand = convertCommand
            self.__convertMethod = convertMethod
            self.__returning = returning
            self.__atributes = self.__determineAtribute(atributes)
            self.__executeCommand = executeCommand
        
        def __determineAtribute(self, atributes):
            if(type(atributes) == str):
                return atributes.split(',')
            return atributes
        
        def AND(self, *tablesNames):
                if (len(tablesNames) == 0):
                    raise ValueError("Impossível impor uma condição secundária sem uma primária definida. Informe as condições primárias usando o método WHERE.")
                elif (len(tablesNames) == 1) and type(tablesNames[0] == tuple):
                    tablesNames = tablesNames[0]
                self.__commandToDB += f" AND ({self.__convertCommand(tablesNames)})"
                return self

        def OR(self, *tablesNames):
            if (len(tablesNames) == 0):
                raise ValueError("Impossível impor uma condição secundária sem uma primária definida. Informe as condições primárias usando o método WHERE.")
            elif (len(tablesNames) == 1) and type(tablesNames[0] == tuple):
                tablesNames = tablesNames[0]
            self.__commandToDB += f" OR ({self.__convertCommand(tablesNames)})"
            return self
        
        def getFirst(self):
            return self.__executeCommand(command= self.__commandToDB, atributes= self.__atributes, convertMethod= self.__convertMethod, returning = self.__returning).getFirst()
        
        def getAll(self):
            return self.__executeCommand(command= self.__commandToDB, atributes= self.__atributes, convertMethod= self.__convertMethod, returning = self.__returning).getAll()
       
    class _WHERE:
        def __init__(self, executeCommand, commandToDB:str, atributes, storageCommand, convertCommand, convertMethod = None, returning = ''):
            self.__storageCommand = storageCommand
            self.__commandToDB = commandToDB
            self.__convertCommand = convertCommand
            self.__atributes = atributes
            self.__convertMethod = convertMethod
            self.__returning = returning
            self.__executeCommand = executeCommand
        
        def WHERE(self, *tablesNames):
            if len(tablesNames) == 0:
                raise ValueError("Impossível impor uma condição sem atributos, comparadores e valores definidos.")
            elif (len(tablesNames) == 1) and type(tablesNames[0] == tuple):
                tablesNames = tablesNames[0]
            self.__commandToDB += f" WHERE ({self.__convertCommand(tablesNames)})"
            return self.__storageCommand(
                command = self.__commandToDB,
                convertCommand = self.__convertCommand,
                atributes = self.__atributes,
                convertMethod = self.__convertMethod,
                returning = self.__returning,
                executeCommand = self.__executeCommand
                )
            
    class _FROM:
        def __init__(self, executeCommand, commandToDB:str, atributes, storageCommand, convertCommand, lstrListToStr, WHERE, convertMethod = None, returning = ''):
            self.__WHERE = WHERE
            self.__commandToDB = commandToDB
            self.__convertCommand = convertCommand
            self.__storageCommand = storageCommand
            self.__atributes = atributes
            self.__convertMethod = convertMethod
            self.__returning = returning
            self.__executeCommand = executeCommand
            self.__lstrListToStr = lstrListToStr

        def FROM(self, *tablesNames):
            if len(tablesNames) == 0:
                raise ValueError("Impossível impor uma condição sem algum nome de tabela definido.")
            elif (len(tablesNames) == 1) and type(tablesNames[0] == tuple):
                tablesNames = tablesNames[0]
            separator = ","
            self.__commandToDB += f" FROM {self.__lstrListToStr(tablesNames, separator)}"
            return self.__WHERE(
                commandToDB = self.__commandToDB,
                convertCommand = self.__convertCommand,
                storageCommand = self.__storageCommand,
                atributes = self.__atributes,
                returning = self.__returning,
                convertMethod = self.__convertMethod,
                executeCommand = self.__executeCommand
                )
    
    class _JOIN:
        def __init__(self, executeCommand, commandToDB:str, atributes, storageCommand, convertCommand, convertMethod = None, returning = ''):
            self.__storageCommand = storageCommand
            self.__commandToDB = commandToDB
            self.__convertCommand = convertCommand
            self.__atributes = atributes
            self.__convertMethod = convertMethod
            self.__returning = returning
            self.__executeCommand = executeCommand
        
        def ON(self, *tablesNames):
            if len(tablesNames) == 0:
                raise ValueError("Impossível impor uma condição sem atributos, comparadores e valores definidos.")
            elif (len(tablesNames) == 1) and type(tablesNames[0] == tuple):
                tablesNames = tablesNames[0]
            self.__commandToDB += f" ON ({self.__convertCommand(tablesNames)})"
            return self.__storageCommand(
                command = self.__commandToDB,
                convertCommand = self.__convertCommand,
                atributes = self.__atributes,
                convertMethod = self.__convertMethod,
                returning = self.__returning,
                executeCommand = self.__executeCommand
                )
    
    def _find(self, atributes:list, convertMethod = False, getAllTuples = False, toJoin:dict = None):
        self._aspas = "'"
        commandToDB = ''
        atributesToSave = ''
        if(len(atributes) == 0):
            return [{}]
        for atribute in atributes:
            atributesToSave += atribute + ','
        atributesToSave = atributesToSave[:-1] #Remove a ultima vírgula pra evitar erros futuros
        commandToDB = f"SELECT {atributesToSave} from {self.__tableName}"
        if(getAllTuples == True):
            return self._executeCommand(
                command= commandToDB,
                atributes = atributes,
                convertMethod = self._convertToSchema if(convertMethod == True) else None
            )
            
        if(toJoin is not None):
            """
            Estrutura esperada do toJoin:
            {
                "tableName":"nome_da_tabela_secundaria",
                "foreignKey":"chave_primaria_da_tabela_secundaria"
            }
            """
            commandToDB += f" LEFT JOIN {toJoin['tableName']}"
            self._aspas = ""
            return self._JOIN(
                commandToDB = commandToDB,
                convertCommand = self._convertCommand,
                storageCommand = self.__storageCommand,
                atributes = atributes,
                convertMethod = self._convertToSchema if(convertMethod == True) else None,
                returning = f" WHERE {toJoin['foreignKey']} IS NOT NULL;", #O espaço antes é importante
                executeCommand = self._executeCommand
            )
            
        return self._WHERE(
                commandToDB = commandToDB,
                convertCommand = self._convertCommand,
                storageCommand = self.__storageCommand,
                atributes = atributes,
                convertMethod = self._convertToSchema if(convertMethod == True) else None,
                executeCommand = self._executeCommand
            )
        
    def _save(self, atributeEValue:dict, toInsert = True, convertMethod = False, toJoinOnUpdate:str = None): #Tratar atributos inexistentes depois ********
        self._aspas = "'"
        commandToDB = ''
        atributesLength = len(atributeEValue)
        count = 0
        atributesToSave = '' #atributo, atributo
        tablesNamesToSave = '' #'valor', 'valor'
        AtributesEtablesNamesToUpdate = '' #atributo = 'valor'
        for atribute, value in atributeEValue.items():
            value = str(value)
            count += 1
            value = f"'{value}'" if(value is not None) else "NULL" #<-- Necessário pois o banco não interpreta None como Null
            if(count == atributesLength):
                atributesToSave += atribute
                tablesNamesToSave += value
                AtributesEtablesNamesToUpdate += f"{atribute} = {value}"
            else:
                atributesToSave += atribute + ','
                tablesNamesToSave += f"{value},"
                AtributesEtablesNamesToUpdate += f"{atribute} = {value},"
        toReturn = self._lstrListToStr(list(self.__typesAcceptables.keys()), ",")
        #Se for pra inserir
        if(toInsert == True): #Se o objeto ainda não está no banco
            commandToDB = f"INSERT INTO {self.__tableName}({atributesToSave}) VALUES ({tablesNamesToSave}) RETURNING {toReturn}"
            if(not convertMethod):
                return create_dictionary(list(self.__typesAcceptables.keys()), execute(commandToDB))
            return self._convertToSchema(create_dictionary(list(self.__typesAcceptables.keys()), execute(commandToDB)))
       
        #Se for pra atualizar:
        if("updated_on" in self.__typesAcceptables):
            AtributesEtablesNamesToUpdate += ',updated_on = NOW()'
        
        if(toJoinOnUpdate is not None):
            self._aspas = ""
            return self._FROM(
                WHERE= self._WHERE,
                commandToDB = f"UPDATE {toJoinOnUpdate} SET {AtributesEtablesNamesToUpdate}",
                convertCommand = self._convertCommand,
                storageCommand = self.__storageCommand,
                atributes = list(self.__typesAcceptables.keys()),
                returning = f" RETURNING {toReturn}", #O espaço antes é importante
                convertMethod = self._convertToSchema if(convertMethod == True) else None,
                executeCommand = self._executeCommand,
                lstrListToStr = self._lstrListToStr
                )
        
        return self._WHERE(
                commandToDB = f"UPDATE {self.__tableName} SET {AtributesEtablesNamesToUpdate}",
                convertCommand = self._convertCommand,
                storageCommand = self.__storageCommand,
                atributes = list(self.__typesAcceptables.keys()),
                returning = f" RETURNING {toReturn}", #O espaço antes é importante
                convertMethod = self._convertToSchema if(convertMethod == True) else None,
                executeCommand = self._executeCommand
                )
    
    def _remove(self, convertMethod = False, toUse:dict = None):
        """
        Estrutura esperada do toUse
        {
            "tableName":"nome_da_tabela_secundaria",
            "atributesToReturn": ["lista", "de", "atributos", "pra", "retornar"]
        }
        """
        self._aspas = "'"
        commandToDB = ''
        atributes = None
        if(toUse is not None):
            atributes = toUse["atributesToReturn"]
            self._aspas = ""
            commandToDB = f"DELETE FROM {toUse['tableName']} USING {self.__tableName}"
        else:
            atributes = list(self.__typesAcceptables.keys())
            commandToDB = f'DELETE FROM {self.__tableName}'
        toReturn = self._lstrListToStr(atributes, ",")
        return self._WHERE(
                commandToDB = commandToDB,
                convertCommand = self._convertCommand,
                storageCommand = self.__storageCommand,
                atributes = atributes,
                returning = f" RETURNING {toReturn}", #O espaço antes é importante
                convertMethod = self._convertToSchema if(convertMethod == True) else None,
                executeCommand = self._executeCommand
                )