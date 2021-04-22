from execute_db_command import execute
from db_helpers import parametersFilter, valuesVerifier, create_dictionary, create_list_dicitionary
from typing import Final

COMPLETE_VALUES_NAMES: Final = ['cpf', 'name', 'address', 'telephone', 'sex','gender', 'blood', 'birth', 'created_on']

#cis = Cisgender
#trans = Transgender
#non-b = Non-binary



def insert_patient_data(cpf, name, address, telephone, sex, gender, blood, birth):
    atributes, values = parametersFilter(
        ['cpf', 'name', 'address', 'telephone', 'sex', 'gender', 'blood', 'birth'],
        [cpf, name, address, telephone, sex, gender, blood, birth]
    )
    commands = (
        """
       INSERT INTO patients({}) VALUES ({})
       RETURNING {};
        """.format(atributes, values, atributes + ', created_on')
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def update_user_data(key, cpf, name, address, telephone, sex, gender, blood, birth, avertNullData = False):
    commands = (
    f"""
    UPDATE patients SET {valuesVerifier(
        ['cpf', 'name', 'address', 'telephone', 'sex', 'gender', 'blood', 'birth'],
        [cpf, name, address, telephone, sex, gender, blood, birth],
        avertNullData
    )}
    WHERE cpf = '{key}'
    RETURNING cpf, name, address, telephone, sex, gender, blood, birth, created_on;
    """
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def delete_user_data(key):
    commands = (
    f"""
    DELETE from patients
    WHERE cpf = '{key}'
    RETURNING cpf, name, address, telephone, sex, gender, blood, birth, created_on;
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
    SELECT cpf, name, address, telephone, sex, gender, blood, birth, created_on
    from patients
    {toFilterResult}
    """
    )
    if(getAllLines == False):
        return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))
    return create_list_dicitionary(COMPLETE_VALUES_NAMES, execute(commands, True))