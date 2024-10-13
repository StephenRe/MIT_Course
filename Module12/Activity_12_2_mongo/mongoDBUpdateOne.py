from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employees = db.employees

filter = {"LastName":"Rose"}

newvalues = { '$set': { 'Age': 32 } }

employees.update_one(filter, newvalues)

employeeCursor = employees.find(filter)
print(employeeCursor[0])


