from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employees = db.employees

filter = {"LastName":"Rose"}

if employees.find_one(filter):
    print("employee record found:",employees.find_one(filter))
else:
    print("employee record NOT found:",filter)

result = employees.delete_one(filter)
print(result.deleted_count)

if employees.find_one(filter):
    print("employee record found:",employees.find_one(filter))
else:
    print("employee record NOT found:",filter)

for i in employees.find():
    print(i)


