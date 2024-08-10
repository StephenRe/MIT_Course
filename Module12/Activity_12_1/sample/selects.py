import mysql.connector
from datetime import datetime
import uuid
import sys
import yaml
sys.dont_write_bytecode = True



cnx_config_load = yaml.safe_load(open('Activity12_1.yaml'))

config = {
    'host': cnx_config_load['Activity_12_1_config']['host'],
    'user': cnx_config_load['Activity_12_1_config']['user'],
    'password': cnx_config_load['Activity_12_1_config']['password'],
    'database': cnx_config_load['Activity_12_1_config']['db'],
    'auth_plugin': 'mysql_native_password'
}

# cnx = mysql.connector.connect(user='root', 
#     password='MyNewPass',
#     host='127.0.0.1',
#     database='pluto',
#     auth_plugin='mysql_native_password')
cnx = mysql.connector.connect(**config)

# create cursor
cursor = cnx.cursor()

# insert
query = ("SELECT * FROM posts")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    