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

class Rc_metadata_class(Model):
    __table__ = 'rc_metadata_class'

    meta_cls_id = StringField(primary_key=True, default=next_id, ddl='varchar(200)')
    classno = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')
    meta_cls_name = StringField(ddl='varchar(200)')
    meta_cls_py = StringField(ddl='varchar(200)')
    parent_id = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createname = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    updatename = StringField(ddl='varchar(200)')


class Rc_metadata(Model):
    __table__ = 'Rc_metadata'

    meta_id = StringField(primary_key=True, default=next_id, ddl='varchar(200)')
    ministry_no = StringField(ddl='varchar(200)')
    meta_name = StringField(ddl='varchar(200)')
    meta_py = StringField(ddl='varchar(200)')
    meta_cls_id = StringField(ddl='varchar(200)')
    field_name = StringField(ddl='varchar(200)')
    field_name1 = StringField(ddl='varchar(200)')
    field_type = StringField(ddl='varchar(200)')
    field_len = StringField(ddl='varchar(200)')
    meta_define = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    createname = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    updatename = StringField(ddl='varchar(200)')


class ViewMetadataClass(Model):
    __table__ = 'V_metadata_class'

    FLMC = StringField(ddl='varchar(200)')
    FLBM = StringField(primary_key=True, default=next_id, ddl='varchar(200)')
    SFZYX = StringField(ddl='varchar(200)')
    ZWQP = StringField(ddl='varchar(200)')
    FZDW = StringField(ddl='varchar(200)')
    YYXT = StringField(ddl='varchar(200)')
    FLDY = StringField(ddl='varchar(200)')
    SJKB = StringField(ddl='varchar(200)')
    YSSJKB = StringField(ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')



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