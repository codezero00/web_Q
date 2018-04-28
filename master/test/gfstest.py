from pymongo import MongoClient
import gridfs
from PIL import Image
from bson.objectid import ObjectId

db = MongoClient("localhost", 27017).gridfs
fs = gridfs.GridFS(db)
print("server info " + " * " * 40)
print(db.server_info)
# a = fs.put(b"hello world")
# print(a)  # 5ae408cd9f6b8f348c4ab0dd
# print(type(a))

# b = fs.get(ObjectId('5ae3d7c99f6b8f380c76b52c')).read()
# print(b)


z = fs.put(fs.get(ObjectId('5ae3d7c99f6b8f380c76b52c')), filename="foo", bar="baz")
print(z)