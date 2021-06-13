from typing import Final
import io

ENFERMEIRO_FOO:Final = "ENFERMEIRO"
ESTAGIARIO_FOO: Final = "ESTAGIARIO"
ADMINISTRADOR_FOO: Final = "ADMINISTRADOR"
ENFERMEIRO_CHEFE_FOO: Final = "ENFERMEIRO_CHEFE"

def valuesVerifier(params, values, avertNullData):
    valuesLength = len(values)
    paramsLength = len(params)
    minLength = valuesLength if (valuesLength < paramsLength) else paramsLength
    pv = ''
    i = 1
    for i in range(0, minLength - 1, 1):
        if(avertNullData == False or values[i] is not None):
            value = f"'{values[i]}'" if(values[i] is not None) else 'NULL'
            pv += params[i] + '=' + value + ', '
    if minLength > 0:
        i = minLength - 1
        if(avertNullData == False or values[i] is not None):
            value = f"'{values[i]}'" if(values[i] is not None) else 'NULL'
            pv += params[i] + '=' + value + ''
    return pv

def parametersFilter(params, values):
    valuesLength = len(values)
    paramsLength = len(params)
    minLength = valuesLength if (valuesLength < paramsLength) else paramsLength
    v = ''
    p = ''
    i = 1
    for i in range(0, minLength - 1, 1):
        if(values[i] is not None):
            v += f"'{values[i]}',"
            p += params[i] + ','
    if minLength > 0:
        v += f"'{values[minLength - 1]}'"
        p += params[minLength - 1]
    return [p, v]

def create_dictionary(keys:list, values:list):
    if(values is not None and keys is not None):
        dictionary = {}
        valuesLength = len(values)
        paramsLength = len(keys)
        minLength = valuesLength if (valuesLength < paramsLength) else paramsLength
        for i in range(0, minLength, 1):
            dictionary[keys[i]] = values[i]
        return dictionary
    return {}

def create_list_dicitionary(keys:list, values:list):
    if(values is not None and keys is not None):
        listDictionary = []
        for i in range(0, len(values), 1):
            listDictionary.append(create_dictionary(keys, values[i]))
        return listDictionary
    return []

def dictToSQLConditions(attAndValues:dict, conector_AND = True, simbol_compare = "="):
        storeV = []
        conector = "AND" if(conector_AND == True) else "OR"
        for key, value in attAndValues.items():
            storeV.append(key)
            storeV.append(simbol_compare)
            storeV.append(value)
            storeV.append(conector)
        storeV.pop(-1)
        return tuple(storeV)
    
def cpfNumber_int_to_str(CPF:int):
    CPF_str = "00000000000"
    CPF = str(CPF)
    min_len = len(CPF)
    max_len = len(CPF_str)
    return CPF_str[: max_len - min_len] + CPF

def read_file(filePath:str, toIgnore:str = None): #<-- Adicionar tratamento de exceção depois *****
    def contain_end_command(line:str, end_simbol = ";"):
        if(len(line) == 1):
            line[0] == end_simbol
        elif(line[-1] == "\n"): #Se tiver quebra de linha (não for a última):
            return line[-2] == end_simbol
        #Se for a última:
        return line[-1] == end_simbol
    
    fileData = ''
    arq = io.open(filePath, "r", encoding="utf8")
    if(toIgnore):
        verifyNextLn = False
        endLineSeq = 0 #qtd de '\n'
        for line in arq:
            if(line[0] == "\n"):
                endLineSeq += 1
            else:
                endLineSeq = 0
            if(endLineSeq < 2): #Tratamento para evitar muitas linhas sequenciais em branco
                if(verifyNextLn):
                    if(contain_end_command(line)):
                        verifyNextLn = False
                elif(not toIgnore.lower() in line.lower()):
                    fileData += line
                else:
                    verifyNextLn = True
    else:
        for line in arq:
            fileData += line
    arq.close()
    return fileData;

def create_file(filePath:str, content:str, writeMode = 'x'): #usar x ou w?
    try:
        arq = io.open(filePath, writeMode, encoding="utf8")
        arq.write(content)
        arq.close()
        return True
    except(Exception) as e:
        print(e)
        return False
        
def lstrListToStr(list, separator:str):
        if(type(list) == str):
            return list
        result = ''
        for item in list:
            assert(type(separator) == str)
            result += item + separator
        return result[:-1] #<-- Removendo ultimo separador
    