"""
select concat(column_name,"= StringField(ddl='varchar(200)')")
from INFORMATION_SCHEMA.COLUMNS
where table_name='etljobs' and table_schema='zyjs_dwc';

"""

import time
import uuid
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
    MCID = StringField(ddl='varchar(200)')
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

    rbid = StringField(primary_key=True, ddl='varchar(200)')
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


class VDBTableLayerTree(Model):
    __table__ = 'v_dbtablelayertree'

    ID = StringField(primary_key=True, ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')
    NAME = StringField(ddl='varchar(200)')
    ISRESOURCE = StringField(ddl='varchar(200)')


class VDBTable(Model):
    __table__ = 'v_dbtable'

    TABID = StringField(primary_key=True, ddl='varchar(200)')
    RBID = StringField(ddl='varchar(200)')
    DLID = StringField(ddl='varchar(200)')
    RESNAME = StringField(ddl='varchar(200)')
    DLNAME = StringField(ddl='varchar(200)')
    TABLENAMEYW = StringField(ddl='varchar(200)')
    TABLENAMEZW = StringField(ddl='varchar(200)')
    REMARK = StringField(ddl='varchar(200)')
    CREATEUSERID = StringField(ddl='varchar(200)')
    CREATETIME = StringField(ddl='varchar(200)')
    UPDATEUSERID = StringField(ddl='varchar(200)')
    UPDATETIME = StringField(ddl='varchar(200)')


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


class VEtlJobs(Model):
    __table__ = 'v_etljobs'

    JBID = StringField(primary_key=True, ddl='varchar(200)')
    NAME = StringField(ddl='varchar(200)')
    REMARK = StringField(ddl='varchar(200)')
    CLIENTNAME = StringField(ddl='varchar(200)')
    URL = StringField(ddl='varchar(200)')
    CREATETIME = StringField(ddl='varchar(200)')


class VDataLayer(Model):
    __table__ = 'v_datalayer'

    DLID = StringField(ddl='varchar(200)', primary_key=True)
    NAME = StringField(ddl='varchar(200)')
    SHORTNAME = StringField(ddl='varchar(200)')
    EFFECT = StringField(ddl='varchar(200)')
    REMARK = StringField(ddl='varchar(200)')
    STATUS = StringField(ddl='varchar(200)')


class VFrontBase(Model):
    __table__ = 'v_frontbase'

    FBID = StringField(ddl='varchar(200)', primary_key=True)
    NAME = StringField(ddl='varchar(200)')
    IP = StringField(ddl='varchar(200)')
    USESOFTWARE = StringField(ddl='varchar(200)')
    LOCATION = StringField(ddl='varchar(200)')
    DEPT = StringField(ddl='varchar(200)')
    EFFECT = StringField(ddl='varchar(200)')
    REMARK = StringField(ddl='varchar(200)')
    STATUS = StringField(ddl='varchar(200)')


class VBloodVertex(Model):
    __table__ = 'v_bloodvertex'

    ID = StringField(ddl='varchar(200)', primary_key=True)
    NAME = StringField(ddl='varchar(200)')
    TYPE = StringField(ddl='varchar(200)')
    COLOR = StringField(ddl='varchar(200)')
    SIZE = StringField(ddl='varchar(200)')


class VBloodEdge(Model):
    __table__ = 'v_bloodedge'

    SRCID = StringField(ddl='varchar(200)', primary_key=True)
    DSTID = StringField(ddl='varchar(200)')
    RELATION = StringField(ddl='varchar(200)')


class VBloodRelation(Model):
    __table__ = 'v_bloodrelation'

    BEID = StringField(ddl='varchar(200)', primary_key=True)
    SRCTABLEID = StringField(ddl='varchar(200)')
    SRCTABLENAME = StringField(ddl='varchar(200)')
    SRCCOLUMNID = StringField(ddl='varchar(200)')
    SRCCOLUMNNAME = StringField(ddl='varchar(200)')
    DSTTABLEID = StringField(ddl='varchar(200)')
    DSTTABLENAME = StringField(ddl='varchar(200)')
    DSTCOLUMNID = StringField(ddl='varchar(200)')
    DSTCOLUMNNAME = StringField(ddl='varchar(200)')


class MetaDataClass(Model):
    __table__ = 'metadataclass'

    mcid = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    metaclsno = StringField(ddl='varchar(200)')
    classno = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')
    metaclsname = StringField(ddl='varchar(200)')
    metaclspy = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    app = StringField(ddl='varchar(200)')
    createname = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)')


class MetaData(Model):
    __table__ = 'MetaData'

    metaid = StringField(primary_key=True, ddl='varchar(200)')
    metaclsid = StringField(ddl='varchar(200)')
    resourceno = StringField(ddl='varchar(200)')
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


class FrontBase(Model):
    __table__ = 'frontbase'

    fbid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    usesoftware = StringField(ddl='varchar(200)')
    location = StringField(ddl='varchar(200)')
    dept = StringField(ddl='varchar(200)')
    effect = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class ResourceBase(Model):
    __table__ = 'resourcebase'

    rbid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    datasourceunit = StringField(ddl='varchar(200)')
    createunit = StringField(ddl='varchar(200)')
    contact = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class DataLayer(Model):
    __table__ = 'datalayer'

    dlid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    shortname = StringField(ddl='varchar(200)')
    effect = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')
    sort = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class DBTable(Model):
    __table__ = 'dbtable'

    tabid = StringField(primary_key=True, ddl='varchar(200)')
    rbid = StringField(ddl='varchar(200)')
    dlid = StringField(ddl='varchar(200)')
    tablenameyw = StringField(ddl='varchar(200)')
    tablenamezw = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class DBTableColumn(Model):
    __table__ = 'dbtablecolumn'

    colid = StringField(primary_key=True, ddl='varchar(200)')
    tabid = StringField(ddl='varchar(200)')
    metaid = StringField(ddl='varchar(200)')
    ispk = StringField(ddl='varchar(200)')
    isnull = StringField(ddl='varchar(200)')
    isuq = StringField(ddl='varchar(200)')
    range = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class ETLClients(Model):
    __table__ = 'etlclients'

    etlid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    port = StringField(ddl='varchar(200)')
    url = StringField(ddl='varchar(200)')
    version = StringField(ddl='varchar(200)')
    location = StringField(ddl='varchar(200)')
    desc = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class ETLJobs(Model):
    __table__ = 'etljobs'

    jbid = StringField(primary_key=True, ddl='varchar(200)')
    etlid = StringField(ddl='varchar(200)')
    jobnum = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    lastlogtime = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')


class BloodEdge(Model):
    __table__ = 'bloodedge'

    beid = StringField(ddl='varchar(200)', primary_key=True)
    srcid = StringField(ddl='varchar(200)')
    dstid = StringField(ddl='varchar(200)')
    relation = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)', default=1)


class VDBTableColumnTree(Model):
    __table__ = 'v_dbtablecolumntree'

    ID = StringField(primary_key=True, ddl='varchar(200)')
    PID = StringField(ddl='varchar(200)')
    NAME = StringField(ddl='varchar(200)')


class NosqlDatabase(Model):
    __table__ = 'nosqlbase'

    ndid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    describe = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    port = StringField(ddl='varchar(200)')
    accountnumber = StringField(ddl='varchar(200)')
    password = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)')


class VNosqlDatabase(Model):
    __table__ = 'v_nosqlbase'

    ndid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    describe = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    port = StringField(ddl='varchar(200)')
    accountnumber = StringField(ddl='varchar(200)')
    password = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    isdel = StringField(ddl='varchar(200)')

# region ggg

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

# endregion
