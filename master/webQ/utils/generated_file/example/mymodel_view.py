import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class V_BLOODEDGE(Model):
    __table__ = 'v_bloodedge'
    srcid = StringField(primary_key=True, ddl='varchar(200)')
    dstid = StringField(ddl='varchar(200)')
    relation = StringField(ddl='varchar(200)')


class V_BLOODRELATION(Model):
    __table__ = 'v_bloodrelation'
    beid = StringField(primary_key=True, ddl='varchar(200)')
    srctableid = StringField(ddl='varchar(200)')
    srctablename = StringField(ddl='varchar(200)')
    srccolumnid = StringField(ddl='varchar(200)')
    srccolumnname = StringField(ddl='varchar(200)')
    dsttableid = StringField(ddl='varchar(200)')
    dsttablename = StringField(ddl='varchar(200)')
    dstcolumnid = StringField(ddl='varchar(200)')
    dstcolumnname = StringField(ddl='varchar(200)')


class V_BLOODVERTEX(Model):
    __table__ = 'v_bloodvertex'
    id = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    color = StringField(ddl='varchar(200)')
    size = StringField(ddl='varchar(200)')


class V_DATALAYER(Model):
    __table__ = 'v_datalayer'
    dlid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    shortname = StringField(ddl='varchar(200)')
    effect = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')


class V_DBTABLE(Model):
    __table__ = 'v_dbtable'
    tabid = StringField(primary_key=True, ddl='varchar(200)')
    rbid = StringField(ddl='varchar(200)')
    dlid = StringField(ddl='varchar(200)')
    resname = StringField(ddl='varchar(200)')
    dlname = StringField(ddl='varchar(200)')
    shortname = StringField(ddl='varchar(200)')
    tablenameyw = StringField(ddl='varchar(200)')
    tablenamezw = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')


class V_DBTABLECOLUMN(Model):
    __table__ = 'v_dbtablecolumn'
    colid = StringField(primary_key=True, ddl='varchar(200)')
    tabid = StringField(ddl='varchar(200)')
    metaid = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    metadefine = StringField(ddl='varchar(200)')
    columntype = StringField(ddl='varchar(200)')
    columnlen = StringField(ddl='varchar(200)')
    ispk = StringField(ddl='varchar(200)')
    isnull = StringField(ddl='varchar(200)')
    isuq = StringField(ddl='varchar(200)')
    range = StringField(ddl='varchar(200)')


class V_DBTABLECOLUMN2(Model):
    __table__ = 'v_dbtablecolumn2'
    colid = StringField(primary_key=True, ddl='varchar(200)')
    tabid = StringField(ddl='varchar(200)')
    metaid = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    len = StringField(ddl='varchar(200)')
    ispk = StringField(ddl='varchar(200)')
    isnull = StringField(ddl='varchar(200)')
    isuq = StringField(ddl='varchar(200)')
    range = StringField(ddl='varchar(200)')


class V_DBTABLECOLUMN3(Model):
    __table__ = 'v_dbtablecolumn3'
    colid = StringField(primary_key=True, ddl='varchar(200)')
    tabid = StringField(ddl='varchar(200)')
    metaid = StringField(ddl='varchar(200)')
    tablenamezw = StringField(ddl='varchar(200)')
    tablenameyw = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    metadefine = StringField(ddl='varchar(200)')
    columntype = StringField(ddl='varchar(200)')
    columnlen = StringField(ddl='varchar(200)')
    ispk = StringField(ddl='varchar(200)')
    isnull = StringField(ddl='varchar(200)')
    isuq = StringField(ddl='varchar(200)')
    range = StringField(ddl='varchar(200)')


class V_DBTABLECOLUMNTREE(Model):
    __table__ = 'v_dbtablecolumntree'
    __tree__ = True
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')


class V_DBTABLELAYERTREE(Model):
    __table__ = 'v_dbtablelayertree'
    __tree__ = True
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    sort = StringField(ddl='varchar(200)')


class V_DBTABLETREE(Model):
    __table__ = 'v_dbtabletree'
    __tree__ = True
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')


class V_FRONTBASE(Model):
    __table__ = 'v_frontbase'
    fbid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    usesoftware = StringField(ddl='varchar(200)')
    location = StringField(ddl='varchar(200)')
    dept = StringField(ddl='varchar(200)')
    effect = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')


class V_JSONTABLESTRUCTARRAY(Model):
    __table__ = 'v_jsontablestructarray'
    rn = StringField(primary_key=True, ddl='varchar(200)')
    tablestructarray = StringField(ddl='varchar(200)')


class V_METADATA(Model):
    __table__ = 'v_metadata'
    resourceno = StringField(ddl='varchar(200)')
    standardno = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    oldcolumnname = StringField(ddl='varchar(200)')
    metaname = StringField(ddl='varchar(200)')
    metapy = StringField(ddl='varchar(200)')
    columnlen = StringField(ddl='varchar(200)')
    columntype = StringField(ddl='varchar(200)')
    metadefine = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    metaid = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')


class V_METADATACLASS(Model):
    __table__ = 'v_metadataclass'
    metaclsname = StringField(ddl='varchar(200)')
    metaclsno = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')
    metaclspy = StringField(ddl='varchar(200)')
    createname = StringField(ddl='varchar(200)')
    app = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    dbtable = StringField(ddl='varchar(200)')
    olddbtable = StringField(ddl='varchar(200)')
    mcid = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')


class V_METADATATREE(Model):
    __table__ = 'v_metadatatree'
    __tree__ = True
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    columnname = StringField(ddl='varchar(200)')
    columntype = StringField(ddl='varchar(200)')
    columnlen = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')


class V_NOSQLBASE(Model):
    __table__ = 'v_nosqlbase'
    ndid = StringField(primary_key=True, ddl='varchar(200)')
    dbname = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    ip = StringField(ddl='varchar(200)')
    port = StringField(ddl='varchar(200)')
    accountnumber = StringField(ddl='varchar(200)')
    password = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')


class V_NOSQLBASETREE(Model):
    __table__ = 'v_nosqlbasetree'
    __tree__ = True
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    isresource = StringField(ddl='varchar(200)')


class V_RESOURCEBASE(Model):
    __table__ = 'v_resourcebase'
    rbid = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    datasourceunit = StringField(ddl='varchar(200)')
    createunit = StringField(ddl='varchar(200)')
    contact = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    status = StringField(ddl='varchar(200)')
