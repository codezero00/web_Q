import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class AUDIT_RECORD_INFO(Model):
	__table__ = 'audit_record_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_note = StringField(ddl='varchar(200)')
	b_id = StringField(ddl='varchar(200)')
	b_type = StringField(ddl='varchar(200)')
	res_name = StringField(ddl='varchar(200)')
	submit_department = StringField(ddl='varchar(200)')


class COLUMN_EDGE(Model):
	__table__ = 'column_edge'
	source_dbtablecolumn_id = StringField(ddl='varchar(200)')
	desc_dbtablecolumn_id = StringField(ddl='varchar(200)')
	rel = StringField(ddl='varchar(200)')
	id = StringField(primary_key=True,ddl='varchar(200)')


class DATA_ITEM_INFO(Model):
	__table__ = 'data_item_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	data_item_code = StringField(ddl='varchar(200)')
	name_zh = StringField(ddl='varchar(200)')
	name_en = StringField(ddl='varchar(200)')
	length = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	resource_info_id = StringField(ddl='varchar(200)')


class DATA_ITEM_INFO_HAS_RESOURCE_COLUMN(Model):
	__table__ = 'data_item_info_has_resource_column'
	id = StringField(primary_key=True,ddl='varchar(200)')
	data_item_info_id = StringField(ddl='varchar(200)')
	resource_column_id = StringField(ddl='varchar(200)')
	resource_column_name = StringField(ddl='varchar(200)')


class DATA_ITEM_INFO_TMP(Model):
	__table__ = 'data_item_info_tmp'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	data_item_code = StringField(ddl='varchar(200)')
	name_zh = StringField(ddl='varchar(200)')
	name_en = StringField(ddl='varchar(200)')
	length = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	resource_info_id = StringField(ddl='varchar(200)')


class DATA_SOURCE_INFO(Model):
	__table__ = 'data_source_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	connect_url = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')
	sql_segment = StringField(ddl='varchar(200)')
	schema_name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	node_info_id = StringField(ddl='varchar(200)')
	realm_info_id = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')


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
	row_num = StringField(ddl='varchar(200)')
	di_model_id = StringField(ddl='varchar(200)')


class DBTABLE_EDGE(Model):
	__table__ = 'dbtable_edge'
	source_dbtable_tabid = StringField(ddl='varchar(200)')
	dest_dbtable_tabid = StringField(ddl='varchar(200)')
	rel = StringField(ddl='varchar(200)')
	id = StringField(primary_key=True,ddl='varchar(200)')


class DBTABLE_HAS_SEC_GROUP(Model):
	__table__ = 'dbtable_has_sec_group'
	dbtable_tabid = StringField(ddl='varchar(200)')
	sec_group_id = StringField(ddl='varchar(200)')
	id = StringField(primary_key=True,ddl='varchar(200)')


class DBTABLE_RELATION(Model):
	__table__ = 'dbtable_relation'
	id = StringField(primary_key=True,ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	primary_dbtablecolumn_colid = StringField(ddl='varchar(200)')
	slave_dbtablecolumn_colid = StringField(ddl='varchar(200)')


class DBTABLECOLUMN(Model):
	__table__ = 'dbtablecolumn'
	colid = StringField(primary_key=True,ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	metaid = StringField(ddl='varchar(200)')
	ispk = StringField(ddl='varchar(200)')
	isnull = StringField(ddl='varchar(200)')
	isuq = StringField(ddl='varchar(200)')
	range = StringField(ddl='varchar(200)')


class DC_GROUP(Model):
	__table__ = 'dc_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	effect = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class DC_SCRIPT_DEVELOPMENT(Model):
	__table__ = 'dc_script_development'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	effect = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	filename = StringField(ddl='varchar(200)')
	dc_group_id = StringField(ddl='varchar(200)')


class DC_SCRIPT_RUN_LOG(Model):
	__table__ = 'dc_script_run_log'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	dc_script_development_id = StringField(ddl='varchar(200)')
	begintime = StringField(ddl='varchar(200)')
	endtime = StringField(ddl='varchar(200)')


class DC_SCRIPT_RUN_LOG_HAS_DBTABLE(Model):
	__table__ = 'dc_script_run_log_has_dbtable'
	dc_script_run_log_id = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	id = StringField(primary_key=True,ddl='varchar(200)')


class DI_MODEL(Model):
	__table__ = 'di_model'
	id = StringField(primary_key=True,ddl='varchar(200)')
	data_connect_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	datalayer = StringField(ddl='varchar(200)')
	table_num = StringField(ddl='varchar(200)')
	data_volume = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class EX_BRIDGE_INFO(Model):
	__table__ = 'ex_bridge_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	source_db_name = StringField(ddl='varchar(200)')
	source_db_type = StringField(ddl='varchar(200)')
	source_table_name = StringField(ddl='varchar(200)')
	source_table_num = StringField(ddl='varchar(200)')
	target_db_name = StringField(ddl='varchar(200)')
	target_db_type = StringField(ddl='varchar(200)')
	target_table_name = StringField(ddl='varchar(200)')
	target_table_num = StringField(ddl='varchar(200)')
	trans_name = StringField(ddl='varchar(200)')
	job_name = StringField(ddl='varchar(200)')
	source_db_id = StringField(ddl='varchar(200)')
	source_table_id = StringField(ddl='varchar(200)')
	target_db_id = StringField(ddl='varchar(200)')
	target_table_id = StringField(ddl='varchar(200)')
	transition_id = StringField(ddl='varchar(200)')
	job_id = StringField(ddl='varchar(200)')
	node_info_id = StringField(ddl='varchar(200)')
	realm_info_id = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class EXCHANGE_REALM(Model):
	__table__ = 'exchange_realm'
	id = StringField(primary_key=True,ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class EXCHANGE_TRANS(Model):
	__table__ = 'exchange_trans'
	id = StringField(primary_key=True,ddl='varchar(200)')
	realm_code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	type2 = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	filepath = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


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
	ic_resource_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	runcycle = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	script = StringField(ddl='varchar(200)')


class IC_RESOURCE(Model):
	__table__ = 'ic_resource'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	ic_resource_group_id = StringField(ddl='varchar(200)')
	hostip = StringField(ddl='varchar(200)')
	cpu = StringField(ddl='varchar(200)')
	memory = StringField(ddl='varchar(200)')
	harddisk = StringField(ddl='varchar(200)')
	other = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')


class IC_RESOURCE_GROUP(Model):
	__table__ = 'ic_resource_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	nettype = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	ip = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')
	servicename = StringField(ddl='varchar(200)')
	port = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE(Model):
	__table__ = 'ic_source_database'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	datasourcename = StringField(ddl='varchar(200)')
	datasourcetype = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	hostip = StringField(ddl='varchar(200)')
	databasename = StringField(ddl='varchar(200)')
	dataport = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE_TABLE(Model):
	__table__ = 'ic_source_database_table'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	ic_source_database_id = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class IC_SOURCE_DATABASE_TABLE_COLUMN(Model):
	__table__ = 'ic_source_database_table_column'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	ic_source_database_table_id = StringField(ddl='varchar(200)')
	metadata_metaid = StringField(ddl='varchar(200)')
	ispk = StringField(ddl='varchar(200)')
	isnull = StringField(ddl='varchar(200)')
	isuq = StringField(ddl='varchar(200)')
	range = StringField(ddl='varchar(200)')
	column_name = StringField(ddl='varchar(200)')
	column_type = StringField(ddl='varchar(200)')
	column_comment = StringField(ddl='varchar(200)')


class MC_DATA_STANDARD(Model):
	__table__ = 'mc_data_standard'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	filepath = StringField(ddl='varchar(200)')


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
	createuserid = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')


class NODE_INFO(Model):
	__table__ = 'node_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


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


class REALM_INFO(Model):
	__table__ = 'realm_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class RESOURCE_AUDITOR(Model):
	__table__ = 'resource_auditor'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	cam_user_id = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')


class RESOURCE_CLASS(Model):
	__table__ = 'resource_class'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	classify = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')
	isleaf = StringField(ddl='varchar(200)')
	isdept = StringField(ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')


class RESOURCE_COLUMN(Model):
	__table__ = 'resource_column'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	length = StringField(ddl='varchar(200)')
	ispk = StringField(ddl='varchar(200)')
	isnull = StringField(ddl='varchar(200)')
	isuq = StringField(ddl='varchar(200)')
	resource_database_table_id = StringField(ddl='varchar(200)')


class RESOURCE_DATABASE(Model):
	__table__ = 'resource_database'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	service_name = StringField(ddl='varchar(200)')
	ip = StringField(ddl='varchar(200)')
	port = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')
	base_name = StringField(ddl='varchar(200)')
	coding = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class RESOURCE_INFO(Model):
	__table__ = 'resource_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	provider_code = StringField(ddl='varchar(200)')
	summary = StringField(ddl='varchar(200)')
	resource_format = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	share_mode = StringField(ddl='varchar(200)')
	share_term = StringField(ddl='varchar(200)')
	isopen = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class RESOURCE_INFO_CHANGE_REQUEST(Model):
	__table__ = 'resource_info_change_request'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	request_title = StringField(ddl='varchar(200)')
	request_department = StringField(ddl='varchar(200)')
	request_user = StringField(ddl='varchar(200)')
	change_type = StringField(ddl='varchar(200)')
	share_term = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')


class RESOURCE_INFO_CHANGE_TMP(Model):
	__table__ = 'resource_info_change_tmp'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	provider_code = StringField(ddl='varchar(200)')
	summary = StringField(ddl='varchar(200)')
	resource_format = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	share_mode = StringField(ddl='varchar(200)')
	share_term = StringField(ddl='varchar(200)')
	isopen = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	resource_info_change_request_id = StringField(ddl='varchar(200)')


class RESOURCE_INFO_DEL(Model):
	__table__ = 'resource_info_del'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	provider_code = StringField(ddl='varchar(200)')
	summary = StringField(ddl='varchar(200)')
	resource_format = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	share_mode = StringField(ddl='varchar(200)')
	share_term = StringField(ddl='varchar(200)')
	isopen = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class RESOURCE_INFO_HAS_RESOURCE_TABLE(Model):
	__table__ = 'resource_info_has_resource_table'
	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_table_id = StringField(ddl='varchar(200)')
	resource_info_id = StringField(ddl='varchar(200)')


class RESOURCE_TABLE(Model):
	__table__ = 'resource_table'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	resource_database_id = StringField(ddl='varchar(200)')


class RESOURCEBASE(Model):
	__table__ = 'resourcebase'
	rbid = StringField(primary_key=True,ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	datasourceunit = StringField(ddl='varchar(200)')
	createunit = StringField(ddl='varchar(200)')
	contact = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')


class ROUTER_INFO(Model):
	__table__ = 'router_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	realm_info_id = StringField(ddl='varchar(200)')


class SC_APPLICATION_RECORD(Model):
	__table__ = 'sc_application_record'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	applicationperson = StringField(ddl='varchar(200)')
	reason = StringField(ddl='varchar(200)')
	purpose = StringField(ddl='varchar(200)')
	applicationtime = StringField(ddl='varchar(200)')
	appstatus = StringField(ddl='varchar(200)')
	appperson = StringField(ddl='varchar(200)')
	sc_service_id = StringField(ddl='varchar(200)')


class SC_GROUP(Model):
	__table__ = 'sc_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	groupname = StringField(ddl='varchar(200)')
	appname = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class SC_LOG(Model):
	__table__ = 'sc_log'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	sc_service_id = StringField(ddl='varchar(200)')
	ip = StringField(ddl='varchar(200)')
	parameters = StringField(ddl='varchar(200)')
	result = StringField(ddl='varchar(200)')
	usetime = StringField(ddl='varchar(200)')
	log = StringField(ddl='varchar(200)')


class SC_SERVICE(Model):
	__table__ = 'sc_service'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	sc_group_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	protocol = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')
	cou = StringField(ddl='varchar(200)')
	method = StringField(ddl='varchar(200)')
	returntype = StringField(ddl='varchar(200)')
	hostaddress = StringField(ddl='varchar(200)')
	apipath = StringField(ddl='varchar(200)')
	returnexample = StringField(ddl='varchar(200)')
	errorcode = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	ispublish = StringField(ddl='varchar(200)')


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


class SEC_GROUP(Model):
	__table__ = 'sec_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class SERVICE_APPLY_INFO(Model):
	__table__ = 'service_apply_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	applicant = StringField(ddl='varchar(200)')
	title = StringField(ddl='varchar(200)')
	app = StringField(ddl='varchar(200)')
	isyj = StringField(ddl='varchar(200)')
	start_time = StringField(ddl='varchar(200)')
	end_time = StringField(ddl='varchar(200)')
	reason = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	audit_userid = StringField(ddl='varchar(200)')
	audit_time = StringField(ddl='varchar(200)')
	service_register_info_id = StringField(ddl='varchar(200)')


class SERVICE_REGISTER_INFO(Model):
	__table__ = 'service_register_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	responsible_person = StringField(ddl='varchar(200)')
	responsible_tel = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	resource_info_id = StringField(ddl='varchar(200)')


class SYS_DICT(Model):
	__table__ = 'sys_dict'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	sort = StringField(ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')


class SYS_USERS_HAS_DBTABLE(Model):
	__table__ = 'sys_users_has_dbtable'
	sys_users_id = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	id = StringField(primary_key=True,ddl='varchar(200)')


class SYS_USERS_HAS_SEC_GROUP(Model):
	__table__ = 'sys_users_has_sec_group'
	id = StringField(primary_key=True,ddl='varchar(200)')
	sys_users_id = StringField(ddl='varchar(200)')
	sec_group_id = StringField(ddl='varchar(200)')
	expiredata = StringField(ddl='varchar(200)')


class TAG_INFO(Model):
	__table__ = 'tag_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class TASK_HOST_INFO(Model):
	__table__ = 'task_host_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	ip = StringField(ddl='varchar(200)')
	host = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')
	url = StringField(ddl='varchar(200)')


class TASK_INFO(Model):
	__table__ = 'task_info'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	job_id = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class USERS(Model):
	__table__ = 'users'
	id = StringField(primary_key=True,ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')
	passwd = StringField(ddl='varchar(200)')
	admin = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	image = StringField(ddl='varchar(200)')
	created_at = StringField(ddl='varchar(200)')


