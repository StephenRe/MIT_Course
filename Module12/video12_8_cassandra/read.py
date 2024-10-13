from cassandra.cluster import Cluster

cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('employees', wait_for_all_pools=True)
session.execute('USE employees')
rows = session.execute('SELECT * FROM EMPLOYEE')
for row in rows:
    print(row)