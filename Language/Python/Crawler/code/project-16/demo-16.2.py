#用户验证
import pymongo
#一：
client = pymongo.MongoClient()
db_auth = client.admin
db_auth.authenticate(username, password)
#连接db数据库
db = client['DB']
#用户验证二
client = MongoClient('mongodb://username:password@localhost:27017/')
db = client['DB']
