# pip install pymongo
import pymongo
from pymongo import MongoClient
import mysqldb

# make a connection
client = MongoClient('mongodb://localhost:1800/final_mongo_container')

# get database
db = client.pluto

# get collection
posts = db.posts

stamps = mysqldb.read()

# write to posts collection
def write(stamps):
    for stamp in stamps:
        item = {
            'stamp': stamp
        }
        db.posts.update_one(item, {'$set':item}, upsert=True)

# read posts collection
def read():
    stamps = []
    # get last 5 entries    
    for post in posts.find().sort('stamp',pymongo.DESCENDING).limit(5):
        stamps.append(post['stamp'])
    return stamps

# delete posts collection data
def delete():
    posts.remove({}) 

def status(stamps,db):
    # print(f'Data in {db}:')
    for stamp in stamps:
        print(stamp)


# status(stamps,'mysql')
# write(stamps)
# print(read())