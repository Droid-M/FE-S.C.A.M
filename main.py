import users_table, patiente_table, create_tables, medical_records_table
from datetime import datetime

#%d/%m/%y %H:%M:%S

if __name__ == '__main__':
    #EXAMPLES TO TEST:

    #create_tables.create_all()
    #print(users_table.insert_user_data("1", "Ana", "", "Ana@gmail.com", "123", "nurse"))
    #print(update_user_data("1", None, None, None, None, None, "nurse", True))
    #print(users_table.insert_user_data("2", "João", "de Tal", "João@gmail.com", "321", "admin"))
    #print(users_table.insert_user_data("3", "Marcia", None, "Marcia@gmail.com", "123", "i_nurse"))
    #print(users_table.delete_user_data('3'))
    #print(select_user_data())
    """
    print(patiente_table.insert_patient_data('1', 'João', 
        None, 
        None, 
        None, 
        None, 
        None, 
        datetime.strptime('21/02/1969', '%d/%m/%Y').date()
        ))
    """
    """
    print(patiente_table.insert_patient_data(
        '8', 
        'Maria das Dores', 
        'Rua das Flores', 
        '75988xxxxxx', 
        'f', 
        'cis', 
        'o+', 
        datetime.strptime('21/02/1969', '%d/%m/%Y').date()
        ))
    """
    """
    print(patiente_table.update_user_data(
        "8",
        '3', 
        'Maria das Dores', 
        'Rua das Flores', 
        '75988xxxxxx', 
        'f', 
        'cis', 
        'o+', 
        datetime.strptime('20/02/1969', '%d/%m/%Y').date()
        ))
    """
    #print(patiente_table.select_user_data("3"))
    #print(patiente_table.delete_user_data("8"))


    """
    print(medical_records_table.insert_medical_records_data(
        "3", '10', 'Maria das Dores', 'f', 'cis','o+', 
        datetime.strptime('20/02/1969', '%d/%m/%Y').date(), 
        datetime.strptime('28/01/2021', '%d/%m/%Y').date(), 
        datetime.strptime('08:21:00', '%H:%M:%S').time(), 'Ana'
    ))
    """
    """
    print(medical_records_table.insert_medical_records_data(
        "2", '10', 'João Mourão', 'm', 'cis','b-', 
        datetime.strptime('20/02/1942', '%d/%m/%Y').date(), 
        datetime.strptime('28/01/2021', '%d/%m/%Y').date(), 
        datetime.strptime('08:43:00', '%H:%M:%S').time(), 'Ana'
    ))
    """
    """
    print(medical_records_table.update_medical_records_data(
        "3", '10',
        None, '10', 'Maria das Dores', 'f', 'cis','o+', 
        datetime.strptime('20/02/1969', '%d/%m/%Y').date(), 
        datetime.strptime('28/01/2021', '%d/%m/%Y').date(), 
        datetime.strptime('08:21:02', '%H:%M:%S').time(), 'Ana',
        True
    ))
    """
    #print(medical_records_table.select_medical_records_data('3', '10'))
    #print(medical_records_table.delete_medical_records_data("2", None))