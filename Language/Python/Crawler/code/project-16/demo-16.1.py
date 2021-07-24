import pymongo
from pymongo.mongo_client import MongoClient
#一：
client = pymongo.MongoClient()
#二:
client = pymongo.MongoClient('localhost', 27017)
#三：
client = MongoClient('mongodb://localhost:27017/')
#链接db数据库
db = client['DB']
user_collection = db.user
