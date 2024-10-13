from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employees = db.employees

filter = {"LastName":"Smith"}

print(employees.count_documents(filter), "employee records found for",filter)

result = employees.delete_many(filter)
print('number deleted:',result.deleted_count)

print(employees.count_documents(filter), "employee records found for",filter)

for i in employees.find():
    print(i)


