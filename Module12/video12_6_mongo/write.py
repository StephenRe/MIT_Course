# pip install pymongo
from pymongo import MongoClient
from datetime import datetime
import uuid

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.pluto

# get collection
posts_new = db.posts_new

# document
id = str(uuid.uuid4())
stamp = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item = {
    'id': id,    
    'stamp': stamp
}

employeeCollection = [
    {"FirstName":"John", "LastName":"Smith", "Age":25},
    {"FirstName":"Peter", "LastName":"Smith", "Age":26},
    {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},
    {"FirstName":"Penny", "LastName":"Lane", "Age":22},
    {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},
    {"FirstName":"Helen", "LastName":"Rose", "Age":23}
]

# insert document
results = posts_new.insert_many(employeeCollection)

print('inserted ids:', results.inserted_ids)

print(results)

for i in posts_new.find():
    print(i)
