from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employees = db.employees

filter = {"LastName":"Smith"}

newvalues = { '$set': { 'Department': 'Computer Science' } }

employees.update_many(filter, newvalues)

employeeCursor = employees.find(filter)

for i in employeeCursor:
    print(i)