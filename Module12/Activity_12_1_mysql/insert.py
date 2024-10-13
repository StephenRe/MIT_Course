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

cnx = mysql.connector.connect(**config)
# create cursor
cursor = cnx.cursor()

# insert
id = 1
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
query = (f'INSERT INTO `posts` VALUES("{id}","{time}")')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    