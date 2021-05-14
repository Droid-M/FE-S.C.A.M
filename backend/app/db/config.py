from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    dbParams = {}
    if (parser.has_section(section)):
        for param in parser.items(section):
            dbParams[param[0]] = param[1]
    else:
        raise Exception(f'Verifique os dados e a existência do arquivo de configuração do banco de dados [diretório: {filename}] [sessão: {section}]')
    return dbParams