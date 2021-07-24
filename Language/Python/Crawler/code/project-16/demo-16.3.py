# TODO: 添加文档  <18-05-21, Redari-Es> #
import pymongo
import datetime
import re
#创建对象
client = pymongo.MongoClient()
#连接db
db = client['DB']
user_collection = db.user
#设置文档格式
user_info = {
    "_id": 100,
    "author": "Redari-Es",
    "text": "Python爬虫开发",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

#使用insert_one单条添加文档，
user_id = user_collection.insert_one(user_info).inserted_id
print("user id is ", user_id)
user_infos = [
    {
        "_id": 101,
        "author": "Redari-Es",
        "text": "Python爬虫开发",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    },
    {
        "_id": 102,
        "author": "redaries",
        "text": "Python爬虫开发",
        "tags": {
            "db": "Mongodb",
            "lan": "Python",
            "modle": "Pymongo"
        },
        "date": datetime.datetime.utcnow()
    },
]
#
user_id = user_collection.insert_many(user_infos).inserted_ids
print("user id is ", user_id)

#更新文档
"""
user_collection.update({},
                       {"$set": {
                           "author": "Redari-Es",
                           "text": "Python爬虫开发"
                       }})
"""
#查询
find_value = user_collection.find({"_id": 101})
print(list(find_value))

#AND多条查询
find_value = user_collection.find(
    {"$and": [{
        "_id": 101
    }, {
        "author": "Redari-Es"
    }]})
print(list(find_value))

#OR条件查询
find_value = user_collection.find(
    {"$or": [{
        "author": "redaries"
    }, {
        "author": "Redari-Es"
    }]})
print(list(find_value))
"""
$lt 小于
$lte 小于等于
$gt 大于
$gte 大于等于
$in 在符合范围内
$nin 不在符合范围内
"""
#如查找id>100而<102,
find_value = user_collection.find({"_id": {"$gt": 100, "$lt": 102}})
print(list(find_value))
#查找id在[100,101]
find_value = user_collection.find({"_id": {"$in": [100, 101]}})
print(list(find_value))

#实现模糊匹配，用正则
#一：
find_value = user_collection.find({"author": {"$regex": ".*Reda.*"}})
print(list(find_value))
#二：
regex = re.compile(".*Reda.*")
find_value = user_collection.find({"author": regex})
print(list(find_value))
