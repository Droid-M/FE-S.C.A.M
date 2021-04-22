from execute_db_command import execute
from db_helpers import parametersFilter, valuesVerifier, create_dictionary, create_list_dicitionary
from typing import Final

COMPLETE_VALUES_NAMES: Final = ['cpf', 'firt_name', 'last_name', 'email', 'password','userType', 'created_on']

#i_nurse = internal_nurse
#h_nurse = head_nurse

def insert_user_data(cpf, firt_name, last_name, email, password, userType):
    atributes, values = parametersFilter(
        ['cpf', 'firt_name', 'last_name', 'email', 'password', 'type'],
        [cpf, firt_name, last_name, email, password, userType]
    )
    commands = (
        """
       INSERT INTO users({}) VALUES ({})
       RETURNING {};
        """.format(atributes, values, atributes + ', created_on')
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def update_user_data(key, cpf, firt_name, last_name, email, password, userType, avertNullData = False):
    commands = (
    f"""
    UPDATE users SET {valuesVerifier(
        ['cpf', 'firt_name', 'last_name', 'email', 'password', 'type'],
        [cpf, firt_name, last_name, email, password, userType],
        avertNullData
    )}
    WHERE cpf = '{key}'
    RETURNING cpf, firt_name, last_name, email, password, type, created_on;
    """
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def delete_user_data(key):
    commands = (
    f"""
    DELETE from users
    WHERE cpf = '{key}'
    RETURNING cpf, firt_name, last_name, email, password, type, created_on;
    """
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def select_user_data(key):
    toFilterResult = ';'
    getAllLines = True
    if(key is not None):
        toFilterResult = f"WHERE cpf = '{key}';"
        getAllLines = False
    commands = (
    f"""
    SELECT cpf, firt_name, last_name, email, password, type, created_on
    from users
    {toFilterResult}
    """
    )
    if(getAllLines == False):
        return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))
    return create_list_dicitionary(COMPLETE_VALUES_NAMES, execute(commands, True))