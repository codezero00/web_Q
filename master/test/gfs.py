from gevent import monkey

monkey.patch_all()

from pymongo import MongoClient
import gridfs
from PIL import Image
from bson.objectid import ObjectId
from io import StringIO, BytesIO
import threading, time
from pymongo.errors import (AutoReconnect,
                            ConfigurationError,
                            ConnectionFailure,
                            InvalidOperation,
                            InvalidURI,
                            NetworkTimeout,
                            NotMasterError,
                            OperationFailure)


# 文件处理系统
class GFS:
    # 初始化
    def __init__(self, username=None, password=None,dbname = 'gridfs'):
        # print("__init__")
        # self.db = MongoClient("localhost", 27017).gridfs
        self.client = MongoClient('mongodb://127.0.0.1:27017')
        # self.db = self.client['gridfs']
        self.db = self.client[dbname]
        self.fs = gridfs.GridFS(self.db)
        self.col = self.db.fs.files
        # print("server info " + " * " * 40)
        # print(self.db.server_info)

    def find(self, query, projection=None):
        """
        pymongo 查询数据操作
        :param query:
        :param projection:
        :return:
        """
        if projection:
            res = self.col.find(query, projection)
        else:
            res = self.col.find(query)
        return res

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
        return gf

    # 写入2进制流
    def putBytes(self, bytes, name, format="png"):
        """
        用于前端上传文件
        :param bytes: 文件二进制流
        :param name: 文件名称
        :param format: 文件类型
        :return:
        """
        gf = None
        try:
            # data = BytesIO()
            name = "%s.%s" % (name, format)
            # image = Image.open(name)
            # bytes.save(data, format)
            # print "name is %s=======data is %s" % (name, data.getvalue())
            # gf = self.fs.put(data.getvalue(), filename=name, format=format)
            gf = self.fs.put(bytes, filename=name, format=format)
        except Exception as e:
            print("Exception ==>> %s " % e)
        return gf

    # 获得图片
    def get(self, id):
        gf = None
        try:
            gf = self.fs.get(ObjectId(id))
            im = gf.read()  # read the data in the GridFS
            dic = {}
            dic["chunk_size"] = gf.chunk_size
            dic["metadata"] = gf.metadata
            dic["length"] = gf.length
            dic["upload_date"] = gf.upload_date
            dic["name"] = gf.name
            dic["content_type"] = gf.content_type
            # dic["format"] = gf.format
            return (im, dic)
        except Exception as e:
            print(e)
            return (None, None)
        finally:
            if gf:
                gf.close()


if __name__ == '__main__':
    gfs = GFS()
    # print(gfs.get('5ae3d6299f6b8f1714c7fdb5'))
    # x = gfs.find(query={"filename":"1.png"}, projection={})
    # print(x)
    # x=gfs.fs.find({"filename":"1.png"},{}).limit(10).skip(1)
    # print(x)
    # x = gfs.find()
    # x = gfs.find(query={"filename": "1.png"}, projection={"filename": 1}).sort([('uploadDate', -1)]).limit(1)
    # print(x)
    # print(list(x))
    # for y in x:
    #     print(y)

    try:
        # The ismaster command is cheap and does not require auth.
        x = gfs.client.admin.command('listDatabases')
    except ConnectionFailure:
        print("Server not available")
    print(x)
