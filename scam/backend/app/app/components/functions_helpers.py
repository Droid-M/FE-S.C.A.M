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