import os
import sys
import pymysql

def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]    

if(argument == '-create'):
    create('docker run -p 5600:3306 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    sys.exit()



