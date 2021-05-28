import io

def config(filename = 'database.env'):
    f = io.open(filename, 'r', encoding="utf8")
    dbParams = {}
    translator = {
        "POSTGRES_DB":"database",
        "POSTGRES_USER":"user",
        "POSTGRES_PASSWORD":"password",
        "POSTGRES_HOST":"host"
    }
    for param in f:
        param = param.split('=')
        #atributo:
        attr = translator.get(param[0])
        if(attr is None):
            attr = param[0]
        #valor:
        value = param[1]
        value = value if value[-1] != '\n' else value[:-1]
        dbParams[attr] = value
    return dbParams