# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items
for k in r.keys('*'):
    print(k, ':', r.get(k))