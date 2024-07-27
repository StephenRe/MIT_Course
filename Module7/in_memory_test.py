import mysql.connector as mc
import yaml
import pandas as pd

cnx_config_load = yaml.safe_load(open('in_memory_config.yaml'))
config = {
    'host': cnx_config_load['sak_config']['host'],
    'user': cnx_config_load['sak_config']['user'],
    'password': cnx_config_load['sak_config']['password'],
    'database': cnx_config_load['sak_config']['db'],
    'auth_plugin': 'mysql_native_password'
}
sakila_cnx = mc.connect(*config)
query = 'select * from actor'
df = pd.read_sql(query, con = sakila_cnx)
sakila_cnx.close()
print(df)
