#查询嵌入、嵌套文档
import pymongo

find_value = user_collection.find({"tags.db": "Mongodb"})
print(list(find_value))

#查询字段
find_value = user_collection.find({"tags.db.Mongodb": "NoSql"})
print(list(find_value))
