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

class MetaDataClass(Model):
    __table__ = 'metadataclass'

    metaclsid = StringField(primary_key=True, ddl='varchar(200)')
    parentid = StringField(ddl='varchar(200)')
    classno = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')
    metaclsname = StringField(ddl='varchar(200)')
    metaclspy = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createname = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')



class MetaData(Model):
    __table__ = 'MetaData'

    metaid = StringField(primary_key=True, ddl='varchar(200)')
    metaclsid = StringField(ddl='varchar(200)')
    standardno = StringField(ddl='varchar(200)')
    metaname = StringField(ddl='varchar(200)')
    metapy = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    oldcolumnname = StringField(ddl='varchar(200)')
    columntype = StringField(ddl='varchar(200)')
    columnlen = StringField(ddl='varchar(200)')
    metadefine = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')


class VMetadataClass(Model):
    __table__ = 'v_metadataclass'

    FLMC = StringField(ddl='varchar(200)')
    FLBM = StringField(primary_key=True, ddl='varchar(200)')
    SFZYX = StringField(ddl='varchar(200)')
    ZWQP = StringField(ddl='varchar(200)')
    FZDW = StringField(ddl='varchar(200)')
    YYXT = StringField(ddl='varchar(200)')
    FLDY = StringField(ddl='varchar(200)')
    SJKB = StringField(ddl='varchar(200)')
    YSSJKB = StringField(ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')


class VMetaData(Model):
    __table__ = 'v_metadata'

    ZYSXBH = StringField(primary_key=True, ddl='varchar(200)')
    BZBM = StringField(ddl='varchar(200)')
    ZDMC = StringField(ddl='varchar(200)')
    YSZDMC = StringField(ddl='varchar(200)')
    ZYSXZWMC = StringField(ddl='varchar(200)')
    ZYSXZWQP = StringField(ddl='varchar(200)')
    CD = StringField(ddl='varchar(200)')
    LX = StringField(ddl='varchar(200)')
    ZYSXDY = StringField(ddl='varchar(200)')
    BZ = StringField(ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')


class VResourceBase(Model):
    __table__ = 'v_resourcebase'

    DBID = StringField(primary_key=True, ddl='varchar(200)')
    XMMC = StringField(ddl='varchar(200)')
    SJLYDW = StringField(ddl='varchar(200)')
    CJDW = StringField(ddl='varchar(200)')
    LXR = StringField(ddl='varchar(200)')
    LXFS = StringField(ddl='varchar(200)')
    ZT = StringField(ddl='varchar(200)')


class VDBTableTree(Model):
    __table__ = 'v_dbtabletree'

    ID = StringField(primary_key=True, ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')
    NAME = StringField(ddl='varchar(200)')
    ISRESOURCE = StringField(ddl='varchar(200)')

class VDBTable(Model):
    __table__ = 'v_dbtable'

    TABID = StringField(primary_key=True, ddl='varchar(200)')
    RBID = StringField(ddl='varchar(200)')
    SSZYK = StringField(ddl='varchar(200)')
    BYWMC = StringField(ddl='varchar(200)')
    BZWMC = StringField(ddl='varchar(200)')
    MS = StringField(ddl='varchar(200)')
    CJSJ = StringField(ddl='varchar(200)')
    ZHXGSJ = StringField(ddl='varchar(200)')


class VDBTableColumn(Model):
    __table__ = 'v_dbtablecolumn'

    COLID = StringField(primary_key=True, ddl='varchar(200)')
    TABID = StringField(ddl='varchar(200)')
    METAID = StringField(ddl='varchar(200)')
    ZDMC = StringField(ddl='varchar(200)')
    ZWM = StringField(ddl='varchar(200)')
    ZDLX = StringField(ddl='varchar(200)')
    ZDDX = StringField(ddl='varchar(200)')
    ZJ = StringField(ddl='varchar(200)')
    FK = StringField(ddl='varchar(200)')
    WY = StringField(ddl='varchar(200)')
    ZY = StringField(ddl='varchar(200)')

class VETLClients(Model):
    __table__ = 'v_etlclients'

    ID = StringField(primary_key=True, ddl='varchar(200)')
    KHDMC = StringField(ddl='varchar(200)')
    IPDZ = StringField(ddl='varchar(200)')
    SYDK = StringField(ddl='varchar(200)')
    URL = StringField(ddl='varchar(200)')
    BB = StringField(ddl='varchar(200)')
    WZ = StringField(ddl='varchar(200)')
    MS = StringField(ddl='varchar(200)')

class VDataLayer(Model):
    __table__ = 'v_datalayer'

    DLID = StringField(ddl='varchar(200)')
    NAME = StringField(ddl='varchar(200)')
    SHORTNAME = StringField(ddl='varchar(200)')
    EFFECT = StringField(ddl='varchar(200)')
    REMARK = StringField(ddl='varchar(200)')
    STATUS = StringField(ddl='varchar(200)')

class grils(Model):
    __tablename__ = 'girls'

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