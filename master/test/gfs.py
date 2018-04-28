from gevent import monkey
monkey.patch_all()

from pymongo import MongoClient
import gridfs
from PIL import Image
from bson.objectid import ObjectId
from io import StringIO, BytesIO
import threading, time


# 文件处理系统
class GFS:
    # 初始化
    def __init__(self):
        print("__init__")
        self.db = MongoClient("localhost", 27017).gridfs
        self.fs = gridfs.GridFS(self.db)
        print("server info " + " * " * 40)
        print(self.db.server_info)




    # 写入
    def put(self, name, format="png", mime="image"):
        gf = None
        data = None
        try:
            data = BytesIO()
            name = "%s.%s" % (name, format)
            image = Image.open(name)
            image.save(data, format)
            # print "name is %s=======data is %s" % (name, data.getvalue())
            gf = self.fs.put(data.getvalue(), filename=name, format=format)
        except Exception as e:
            print("Exception ==>> %s " % e)
        finally:
            GFS.c = None
            GFS._connect()
        return gf


    # 获得图片
    def get(self, id):
        gf = None
        try:
            gf = GFS.fs.get(ObjectId(id))
            print(gf)
            im = gf.read()  # read the data in the GridFS
            dic = {}
            dic["chunk_size"] = gf.chunk_size
            dic["metadata"] = gf.metadata
            dic["length"] = gf.length
            dic["upload_date"] = gf.upload_date
            dic["name"] = gf.name
            dic["content_type"] = gf.content_type
            dic["format"] = gf.format
            return (im, dic)
        except Exception as e:
            print(e)
            return (None, None)
        finally:
            if gf:
                gf.close()

if __name__=='__main__':
    gfs = GFS.getInstance()
    print(gfs)