import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root', 
    password='MyNewPass',
    host='localhost',
    port='3300',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `mlb_stats`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS mlb_stats")
cursor.execute(query)

# use db
query = ("USE mlb_stats")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE da_playas(
    id VARCHAR(36),
    player_name varchar(100),
    team varchar(3),
    games int,
    at_bats int,
    hits int,
    batting_avg float
)
''')
cursor.execute(query)

query = 'show databases'
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

query = ('''
         insert into da_playas
         values(1, 'Cal Raleigh', 'SEA', 115, 398, 85, .214),
         (2, 'Luke Raley', 'SEA', 103, 302, 69, .228),
         (3, 'Mitch Garver', 'SEA', 97, 312, 52, .167)
         ''')
cursor.execute(query)

query = 'select * from da_playas'
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cnx.commit()
cursor.close()
cnx.close()    