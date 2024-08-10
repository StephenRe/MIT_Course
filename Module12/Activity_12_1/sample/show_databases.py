import mysql.connector
from datetime import datetime
import uuid
import sys
import yaml
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    port=3300,
    host='localhost',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# insert
query = ("SHOW DATABASES")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    