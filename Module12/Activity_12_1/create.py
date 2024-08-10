import mysql.connector
import sys
import yaml
sys.dont_write_bytecode = True

cnx_config_load = yaml.safe_load(open('Activity12_1.yaml'))

config = {
    'host': cnx_config_load['Activity_12_1_config']['host'],
    'user': cnx_config_load['Activity_12_1_config']['user'],
    'password': cnx_config_load['Activity_12_1_config']['password'],
    'database': '',
    'auth_plugin': 'mysql_native_password'
}

cnx = mysql.connector.connect(**config)

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS restaurants;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS restaurants")
cursor.execute(query)

# use db
query = ("USE restaurants")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE posts(
    id VARCHAR(36),
    stamp VARCHAR(20)
)
''')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    