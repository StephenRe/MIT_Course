from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employees = db.employees


employeeCursor = employees.find({"LastName":"Smith"})

for i in employeeCursor:
    print(i)