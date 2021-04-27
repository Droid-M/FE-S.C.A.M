import psycopg2 as toDB
from config import config

def execute(command = None):
    connection = None
    result = None
    try:
        connection = toDB.connect(**config())
        if(command is not None):
            cursor = connection.cursor()
            cursor.execute(command)
            try: #<-- procurar alguma alternativa depois
                result = cursor.fetchall()
            except(Exception, toDB.DatabaseError) as Error1:
                print(Error1)
            cursor.close()
            connection.commit()
    except(Exception, toDB.DatabaseError) as Error2:
        print(Error2)
    finally:
        if(connection is not None):
            connection.close()
    return result