import time, uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = IntegerField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

# class Metadata_detail(Model):
#     __table__ = 'metadata_detail'
#
#     id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
#     pid = StringField(ddl='varchar(50)')
#     zysxbh = StringField(ddl='varchar(50)')
#     bzbm = StringField(ddl='varchar(100)')
#     zdmc = StringField(ddl='varchar(100)')
#     yszdmc = StringField(ddl='varchar(100)')
#     zysxzwmc = StringField(ddl='varchar(100)')
#     zysxzwqp = StringField(ddl='varchar(100)')
#     cd = StringField(ddl='varchar(100)')
#     lx = StringField(ddl='varchar(100)')
#     zysxdy = StringField(ddl='varchar(100)')
#     bz = StringField(ddl='varchar(100)')
#     created_at = FloatField(default=time.time)
#
# class Metadata_group(Model):
#     __table__ = 'metadata_group'
#
#     id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
#     pid = StringField(ddl='varchar(50)')
#     groupname = StringField(ddl='varchar(50)')
#     groupcode = StringField(ddl='varchar(50)')
#     sfzyx = StringField(ddl='varchar(100)')
#     py = StringField(ddl='varchar(50)')
#     fzdw = StringField(ddl='varchar(50)')
#     yyxt = StringField(ddl='varchar(50)')
#     fldy = StringField(ddl='varchar(50)')
#     sjkb = StringField(ddl='varchar(50)')
#     yssjkb = StringField(ddl='varchar(50)')
#     created_at = FloatField(default=time.time)
#
# class ExcelContent(Model):
#     __table__ = 'data_excel_content'
#
#     id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
#     exid = StringField(ddl='varchar(50)')
#     ex_name = StringField(ddl='varchar(50)')
#     ex_column = StringField(ddl='varchar(100)')
#     ex_content = TextField()
#     rnum = IntegerField()





class grils(Model):
    __tablename__='girls'

    girid = StringField(ddl='varchar(50)', primary_key=True)
    name = StringField(ddl='varchar(100)')
    attrs = TextField()
    bname = StringField(ddl='varchar(100)')
    sex = StringField(ddl='varchar(100)')
    height = StringField(ddl='varchar(100)')
    weight = StringField(ddl='varchar(100)')
    bwh = StringField(ddl='varchar(100)')
    birthday = StringField(ddl='varchar(100)')
    age = StringField(ddl='varchar(100)')
    xz = StringField(ddl='varchar(100)')
    birthaddr = StringField(ddl='varchar(100)')
    job = StringField(ddl='varchar(100)')
    hobby = StringField(ddl='varchar(100)')
    detail = TextField()
    createtime = StringField(ddl='varchar(100)')

class ggroup(Model):
    __tablename__ = 'ggroup'
    groid = IntegerField(primary_key=True)
    girid = IntegerField()
    name = StringField(ddl='varchar(100)')
    description = StringField(ddl='varchar(200)')
    url = StringField(ddl='varchar(100)')
    createtime = StringField(ddl='varchar(100)')

class gimages(Model):
    __tablename__ = 'gimages'
    imgid = IntegerField(primary_key=True)
    groid = StringField(ddl='varchar(100)')
    url = StringField(ddl='varchar(100)')
    createtime = StringField(ddl='varchar(100)')

class ginfo(Model):
    __tablename__ = 'ginfo'
    infid = IntegerField(primary_key=True)
    createtime = StringField(ddl='varchar(100)')
    content = TextField()
    title = StringField(ddl='varchar(100)')
    photo = StringField(ddl='varchar(100)')
    type = StringField(ddl='varchar(100)')

class gtype(Model):
    __tablename__ = 'gtype'
    idgtype = IntegerField(primary_key=True)
    girid = IntegerField()
    type = StringField(ddl='varchar(100)')
    createtime = StringField(ddl='varchar(100)')