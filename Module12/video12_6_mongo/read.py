# pip install pymongo
from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.pluto

# get collection
posts_test = db.posts_test

databases = client.list_database_names()
print("Databases:", databases)

collections = db.list_collection_names()
print("Collections:", collections)

# walk through all posts
if posts_test in db.list_collection_names():

    for post in posts_test.find():
        print(post)
else:
    print('nope')
print(posts_test in db.list_collection_names())




