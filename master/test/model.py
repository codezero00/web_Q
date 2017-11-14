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

class Comp(Model):
    __table__ = 'data_comp'

    compid = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    code = StringField(ddl='varchar(50)')
    name = StringField(ddl='varchar(100)')
    remark = StringField(ddl='varchar(2000)')
    created_at = FloatField(default=time.time)

class Excel(Model):
    __table__ = 'data_excel'

    exid = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    compid = StringField(ddl='varchar(50)')
    titile = StringField(ddl='varchar(50)')
    remark = StringField(ddl='varchar(50)')
    file_path = StringField(ddl='varchar(100)')
    upuser = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)

class ExcelContent(Model):
    __table__ = 'data_excel_content'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    exid = StringField(ddl='varchar(50)')
    ex_name = StringField(ddl='varchar(50)')
    ex_column = StringField(ddl='varchar(100)')
    ex_content = TextField()
    rnum = IntegerField()