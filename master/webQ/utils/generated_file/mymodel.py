import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class BLOODEDGE(Model):
	__table__ = 'bloodedge'
	beid = StringField(primary_key=True,ddl='varchar(200)')
	srcid = StringField(ddl='varchar(200)')
	dstid = StringField(ddl='varchar(200)')
	relation = StringField(ddl='varchar(200)')


class DATALAYER(Model):
	__table__ = 'datalayer'
	dlid = StringField(primary_key=True,ddl='varchar(200)')
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


class DBTABLE(Model):
	__table__ = 'dbtable'
	tabid = StringField(primary_key=True,ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	dlid = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class DBTABLE_RELATION(Model):
	__table__ = 'dbtable_relation'
	id = StringField(primary_key=True,ddl='varchar(200)')
	primary_table_id = StringField(ddl='varchar(200)')
	slave_talbe_id = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class DBTABLECOLUMN(Model):
	__table__ = 'dbtablecolumn'
	colid = StringField(primary_key=True,ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	metaid = StringField(ddl='varchar(200)')
	ispk = StringField(ddl='varchar(200)')
	isnull = StringField(ddl='varchar(200)')
	isuq = StringField(ddl='varchar(200)')
	range = StringField(ddl='varchar(200)')


class FRONTBASE(Model):
	__table__ = 'frontbase'
	fbid = StringField(primary_key=True,ddl='varchar(200)')
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


class IC_JOB(Model):
	__table__ = 'ic_job'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class IC_RESOURCE(Model):
	__table__ = 'ic_resource'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class IC_RESOURCE_GROUP(Model):
	__table__ = 'ic_resource_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE(Model):
	__table__ = 'ic_source_database'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE_TABLE(Model):
	__table__ = 'ic_source_database_table'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	ic_source_database_id = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE_TABLE_COLUMN(Model):
	__table__ = 'ic_source_database_table_column'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class METADATA(Model):
	__table__ = 'metadata'
	metaid = StringField(primary_key=True,ddl='varchar(200)')
	mcid = StringField(ddl='varchar(200)')
	resourceno = StringField(ddl='varchar(200)')
	standardno = StringField(ddl='varchar(200)')
	columnname = StringField(ddl='varchar(200)')
	oldcolumnname = StringField(ddl='varchar(200)')
	metaname = StringField(ddl='varchar(200)')
	metapy = StringField(ddl='varchar(200)')
	columntype = StringField(ddl='varchar(200)')
	columnlen = StringField(ddl='varchar(200)')
	metadefine = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class METADATACLASS(Model):
	__table__ = 'metadataclass'
	mcid = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	metaclsno = StringField(ddl='varchar(200)')
	classno = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')
	metaclsname = StringField(ddl='varchar(200)')
	metaclspy = StringField(ddl='varchar(200)')
	app = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	createname = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class NOSQLBASE(Model):
	__table__ = 'nosqlbase'
	ndid = StringField(primary_key=True,ddl='varchar(200)')
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


class RESOURCEBASE(Model):
	__table__ = 'resourcebase'
	rbid = StringField(primary_key=True,ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	datasourceunit = StringField(ddl='varchar(200)')
	createunit = StringField(ddl='varchar(200)')
	contact = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class SC_APPLICATION_RECORD(Model):
	__table__ = 'sc_application_record'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class SC_GROUP(Model):
	__table__ = 'sc_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class SC_LOG(Model):
	__table__ = 'sc_log'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class SC_SERVICE(Model):
	__table__ = 'sc_service'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class SC_SERVICE_REQUEST_PARAMETERS(Model):
	__table__ = 'sc_service_request_parameters'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	location = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	example = StringField(ddl='varchar(200)')
	default = StringField(ddl='varchar(200)')
	required = StringField(ddl='varchar(200)')
	rmark = StringField(ddl='varchar(200)')
	sc_service_id = StringField(ddl='varchar(200)')


class USERS(Model):
	__table__ = 'users'
	id = StringField(primary_key=True,ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')
	passwd = StringField(ddl='varchar(200)')
	admin = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	image = StringField(ddl='varchar(200)')
	created_at = StringField(ddl='varchar(200)')


