from execute_db_command import execute

#i_nurse = internal_nurse
#h_nurse = head_nurse
#(falta definir a TIMEZONE)

def create_all():
    commands = (
        """
        CREATE TYPE USERTYPE AS ENUM ('admin', 'nurse', 'i_nurse', 'h_nurse');
        CREATE TYPE SEXTYPE AS ENUM ('f', 'm');
        CREATE TYPE BLOODTYPE AS ENUM ('a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-', 'null_rh');
        CREATE TYPE GENDERIDENTITY AS ENUM ('cis', 'trans', 'non-b');

        CREATE TABLE users (
            cpf VARCHAR (11) PRIMARY KEY NOT NULL,
            firt_name VARCHAR ( 50 ) NOT NULL,
            last_name VARCHAR ( 100 ) DEFAULT '',
            email VARCHAR ( 255 ) UNIQUE NOT NULL,
            password VARCHAR ( 20 ) NOT NULL,
            created_on TIMESTAMP NOT NULL DEFAULT NOW(),
            type USERTYPE NOT NULL
        );

        CREATE TABLE patients (
            cpf VARCHAR (11) PRIMARY KEY NOT NULL,
            name VARCHAR ( 150 ) NOT NULL,
            address VARCHAR (150),
            telephone VARCHAR (16),
            sex SEXTYPE,
            gender GENDERIDENTITY,
            blood BLOODTYPE,
            birth DATE,
            created_on TIMESTAMP NOT NULL DEFAULT NOW()
        );

         CREATE TABLE medical_records (
            patient_cpf VARCHAR (11),
            h_nurse_cpf VARCHAR (11),
            patient_name VARCHAR (150),
            patient_sex SEXTYPE,
            patient_gender GENDERIDENTITY,
            patient_blood BLOODTYPE,
            patient_birth DATE,
            patient_hospitalization_date DATE,
            patient_scheduling_time TIME,
            nurse_name VARCHAR (150),
            created_on TIMESTAMP NOT NULL DEFAULT NOW(),
            PRIMARY KEY (patient_cpf, h_nurse_cpf)
        );
        """
        #is_active BOOLEAN DEFAULT TRUE
    )
    execute(commands)