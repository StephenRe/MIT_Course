import pymysql

cnx = pymysql.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    port=3306)

cursor = cnx.cursor()

query = ("USE customerdb;")
cursor.execute(query)

query = ('''
INSERT INTO customerdb.customer 
VALUES (2, "Peter Parker", "pp@example.com");
''')
cursor.execute(query)
cnx.commit()
cursor.close()
cnx.close()   