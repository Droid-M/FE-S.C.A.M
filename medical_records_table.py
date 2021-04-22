from execute_db_command import execute
from db_helpers import parametersFilter, valuesVerifier, create_dictionary, create_list_dicitionary
from typing import Final

COMPLETE_VALUES_NAMES: Final = ['patient_cpf', 'h_nurse_cpf', 'patient_name', 'patient_sex', 'patient_gender','patient_blood', 'patient_birth', 'patient_hospitalization_date', 'patient_scheduling_time', 'nurse_name', 'created_on']

def __define_arguments(patient_cpf, h_nurse_cpf):
    argument1 = ""
    argument2 = " "
    conector = ""
    getAllLines = True
    if(patient_cpf is not None):
        argument1 = f"WHERE patient_cpf = '{patient_cpf}'"
        if(h_nurse_cpf is not None):
            getAllLines = False
            conector = " AND "
            argument2 = f"h_nurse_cpf = '{h_nurse_cpf}' "
    elif(h_nurse_cpf is not None):
        argument2 = f"WHERE h_nurse_cpf = '{h_nurse_cpf}' "
    return {'search_keys': (argument1 + conector + argument2), 'isAllLines' : getAllLines}

def insert_medical_records_data(
        patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood, 
        patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name
    ):
    atributes, values = parametersFilter(
        [
            'patient_cpf', 'h_nurse_cpf', 'patient_name', 'patient_sex', 'patient_gender','patient_blood',
            'patient_birth', 'patient_hospitalization_date', 'patient_scheduling_time', 'nurse_name'
        ],
        [
            patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood,
            patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name
        ]
    )
    commands = (
        """
       INSERT INTO medical_records({}) VALUES ({})
       RETURNING {};
        """.format(atributes, values, atributes + ', created_on')
    )
    return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))

def update_medical_records_data(key1, key2,
        patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood, 
        patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name,
        avertNullData = False
    ):
    arguments = __define_arguments(key1, key2)
    commands = (
    f"""
    UPDATE medical_records SET {valuesVerifier(
        [
            'patient_cpf', 'h_nurse_cpf', 'patient_name', 'patient_sex', 'patient_gender','patient_blood',
            'patient_birth', 'patient_hospitalization_date', 'patient_scheduling_time', 'nurse_name'
        ],
        [
            patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood,
            patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name
        ],
        avertNullData
    )}
    {arguments.get("search_keys")}
    RETURNING patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood,
    patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name, created_on;
    """
    )
    if(arguments.get("isAllLines") == False):
        return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))
    return create_list_dicitionary(COMPLETE_VALUES_NAMES, execute(commands, True))

def delete_medical_records_data(patient_cpf, h_nurse_cpf):
    arguments = __define_arguments(patient_cpf, h_nurse_cpf)
    commands = (
    f"""
    DELETE from medical_records
    {arguments.get("search_keys")}
    RETURNING patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood,
    patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name, created_on;
    """
    )
    if(arguments.get("isAllLines") == False):
        return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))
    return create_list_dicitionary(COMPLETE_VALUES_NAMES, execute(commands, True))

def select_medical_records_data(patient_cpf, h_nurse_cpf):
    params = "'patient_cpf', 'h_nurse_cpf', 'patient_name', 'patient_sex', 'patient_gender','patient_blood', 'patient_birth', 'patient_hospitalization_date', 'patient_scheduling_time', 'nurse_name'"
    arguments = __define_arguments(patient_cpf, h_nurse_cpf)
    commands = (
    f"""
    SELECT patient_cpf, h_nurse_cpf, patient_name, patient_sex, patient_gender,patient_blood,
    patient_birth, patient_hospitalization_date, patient_scheduling_time, nurse_name, created_on
    from medical_records
    {arguments.get("search_keys")}
    """
    )
    if(arguments.get("isAllLines") == False):
        return create_dictionary(COMPLETE_VALUES_NAMES, execute(commands))
    return create_list_dicitionary(COMPLETE_VALUES_NAMES, execute(commands, True))