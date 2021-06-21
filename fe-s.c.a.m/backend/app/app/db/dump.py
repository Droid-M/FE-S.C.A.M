#!/usr/bin/python
from time import gmtime, strftime
import subprocess
import os
database_list = [ 'database1', 'database2', 'etc' ]
USER = "postgres"
PASS = "postgres-password"
BACKUP_DIR = "e:\\postgresql_backups\\"
# dump using PostgreSQL's custom format, with maximum compression. (-F c, -Z 9)
dumper = """ "c:\\program files\\postgresql\\8.1\\bin\\pg_dump" -U %s -Z 9 -f %s -F c %s  """                  
os.putenv('PGPASSWORD', PASS)
for database_name in database_list :
        print strftime( "%Y-%m-%d-%H-%M-%S" , gmtime()) + ":dump started for %s"%database_name
        time = str (strftime("%Y-%m-%d-%H-%M"))
        file_name = database_name + '_' + time + ".sql.pgdump"
        #Run the pg_dump command to the right directory
        command = dumper % (USER,  BACKUP_DIR + file_name, database_name)
        subprocess.call(command,shell = True)
        print strftime( "%Y-%m-%d-%H-%M-%S" , gmtime()) + ":finished"