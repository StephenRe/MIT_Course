# pip install redis
import redis
from datetime import datetime

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# write to server
r.mset({'Italy': 'Rome', 'France': 'Paris'})