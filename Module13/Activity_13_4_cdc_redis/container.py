import os
import sys
import pymysql
# uncomment code below for Activity 13.5
#from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql, mongodb does not need it

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# add init_cassandra() below for Activity 13.5


# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='MyNewPass',
        host='127.0.0.1',
        port=3300)

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto;")
    cursor.execute(query)

    # use db
    query = ("USE pluto;")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    );
    ''')
    cursor.execute(query)

    # show DBs
    query = ('''
    show databases
    ''')
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()   

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')
    # Add code to delete "some-redis" for Redis database container for Activity 13.4
    # Add code to delete "some-cassandra" for Cassandra database container for Activity 13.5
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3300:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongo')
    create('docker run -p 6379:6379 --name some-redis -d redis', 'redis')
    # Add code to create the Redis database for Activity 13.4
    # Add code to create the Cassandra database for Activity 13.5
    sys.exit()

# if -init, init mysql, mongodb does not need it
if(argument == '-init'):
    init_mysql()
    # Add call to init_cassandra() to initialize the Cassandra database container. Activity 13.5.
    sys.exit()