from cassandra.cluster import Cluster
keyspace = None
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect(keyspace)

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS employees
    WITH REPLICATION = {'class':'SimpleStrategy','replication_factor' :1};
    """)

session.set_keyspace('employees')

session.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        EMPLOYEE_ID int PRIMARY KEY,
        FIRST_NAME text,
        LAST_NAME text,
        AGE int
    );
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (123450, 'John', 'Doe', 33);
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (123678, 'Mary', 'Jane', 21);
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (678123, 'Peter', 'Gabriel', 65);
""")