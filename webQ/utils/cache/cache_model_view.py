import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class V_XXL_JOB_QRTZ_TRIGGER_INFO(Model):
	__table__ = 'V_XXL_JOB_QRTZ_TRIGGER_INFO'

	id = StringField(primary_key=True,ddl='varchar(200)')
	job_group = StringField(ddl='varchar(200)')
	job_cron = StringField(ddl='varchar(200)')
	job_desc = StringField(ddl='varchar(200)')
	add_time = StringField(ddl='varchar(200)')
	update_time = StringField(ddl='varchar(200)')
	author = StringField(ddl='varchar(200)')
	alarm_email = StringField(ddl='varchar(200)')
	executor_route_strategy = StringField(ddl='varchar(200)')
	executor_handler = StringField(ddl='varchar(200)')
	executor_param = StringField(ddl='varchar(200)')
	executor_block_strategy = StringField(ddl='varchar(200)')
	executor_timeout = StringField(ddl='varchar(200)')
	executor_fail_retry_count = StringField(ddl='varchar(200)')
	glue_type = StringField(ddl='varchar(200)')
	glue_source = StringField(ddl='varchar(200)')
	glue_remark = StringField(ddl='varchar(200)')
	glue_updatetime = StringField(ddl='varchar(200)')
	child_jobid = StringField(ddl='varchar(200)')


class V_XXL_JOB_QRTZ_TRIGGER_LOG(Model):
	__table__ = 'V_XXL_JOB_QRTZ_TRIGGER_LOG'

	id = StringField(primary_key=True,ddl='varchar(200)')
	job_group = StringField(ddl='varchar(200)')
	job_id = StringField(ddl='varchar(200)')
	executor_address = StringField(ddl='varchar(200)')
	executor_handler = StringField(ddl='varchar(200)')
	executor_param = StringField(ddl='varchar(200)')
	executor_sharding_param = StringField(ddl='varchar(200)')
	executor_fail_retry_count = StringField(ddl='varchar(200)')
	trigger_time = StringField(ddl='varchar(200)')
	trigger_code = StringField(ddl='varchar(200)')
	trigger_msg = StringField(ddl='varchar(200)')
	handle_time = StringField(ddl='varchar(200)')
	handle_code = StringField(ddl='varchar(200)')
	handle_msg = StringField(ddl='varchar(200)')
	alarm_status = StringField(ddl='varchar(200)')


class SYS_USERS(Model):
	__table__ = 'sys_users'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	account_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	sex = StringField(ddl='varchar(200)')
	job = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')
	sso_subid = StringField(ddl='varchar(200)')
	file_path = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')


class V_2_METADATATREE(Model):
	__table__ = 'v_2_metadatatree'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	columnname = StringField(ddl='varchar(200)')
	columntype = StringField(ddl='varchar(200)')
	columnlen = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')


class V_AUDIT_RECORD_INFO(Model):
	__table__ = 'v_audit_record_info'

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


class V_CATALOG_CHANGE(Model):
	__table__ = 'v_catalog_change'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_code = StringField(ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	request_department = StringField(ddl='varchar(200)')
	request_title = StringField(ddl='varchar(200)')
	resource_type = StringField(ddl='varchar(200)')
	request_user = StringField(ddl='varchar(200)')
	request_time = StringField(ddl='varchar(200)')
	change_type = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	share_term = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class V_CHANGE_TASK(Model):
	__table__ = 'v_change_task'

	id = StringField(primary_key=True,ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	job_id = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	job_cron = StringField(ddl='varchar(200)')
	job_desc = StringField(ddl='varchar(200)')
	add_time = StringField(ddl='varchar(200)')
	update_time = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')


class V_COLUMN_EDGE(Model):
	__table__ = 'v_column_edge'

	id = StringField(primary_key=True,ddl='varchar(200)')
	source_dbtablecolumn_id = StringField(ddl='varchar(200)')
	desc_dbtablecolumn_id = StringField(ddl='varchar(200)')
	rel = StringField(ddl='varchar(200)')


class V_DATA_ITEM_COMPAR(Model):
	__table__ = 'v_data_item_compar'

	id = StringField(primary_key=True,ddl='varchar(200)')
	data_item_info_id = StringField(ddl='varchar(200)')
	resource_column_id = StringField(ddl='varchar(200)')
	resource_column_name = StringField(ddl='varchar(200)')
	data_item_code = StringField(ddl='varchar(200)')
	name_zh = StringField(ddl='varchar(200)')
	name_en = StringField(ddl='varchar(200)')


class V_DATA_ITEM_INFO(Model):
	__table__ = 'v_data_item_info'

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


class V_DATA_ITEM_INFO_HAS_RESOURCE_COLUMN(Model):
	__table__ = 'v_data_item_info_has_resource_column'

	id = StringField(primary_key=True,ddl='varchar(200)')
	data_item_info_id = StringField(ddl='varchar(200)')
	resource_column_id = StringField(ddl='varchar(200)')
	resource_column_name = StringField(ddl='varchar(200)')


class V_DATA_ITEM_INFO_TMP(Model):
	__table__ = 'v_data_item_info_tmp'

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


class V_DATA_SOURCE_INFO(Model):
	__table__ = 'v_data_source_info'

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
	node_name = StringField(ddl='varchar(200)')
	realm_name = StringField(ddl='varchar(200)')


class V_DBTABLE(Model):
	__table__ = 'v_dbtable'

	id = StringField(primary_key=True,ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	dlid = StringField(ddl='varchar(200)')
	resname = StringField(ddl='varchar(200)')
	dlname = StringField(ddl='varchar(200)')
	shortname = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	row_num = StringField(ddl='varchar(200)')
	data_source_name = StringField(ddl='varchar(200)')
	data_source_type = StringField(ddl='varchar(200)')
	connect_url = StringField(ddl='varchar(200)')
	data_source_info_id = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class V_DBTABLE_EDGE(Model):
	__table__ = 'v_dbtable_edge'

	id = StringField(primary_key=True,ddl='varchar(200)')
	source_dbtable_tabid = StringField(ddl='varchar(200)')
	dest_dbtable_tabid = StringField(ddl='varchar(200)')
	rel = StringField(ddl='varchar(200)')


class V_DBTABLE_HAS_SEC_GROUP(Model):
	__table__ = 'v_dbtable_has_sec_group'

	id = StringField(primary_key=True,ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	sec_group_id = StringField(ddl='varchar(200)')


class V_DBTABLE_RELATION(Model):
	__table__ = 'v_dbtable_relation'

	id = StringField(primary_key=True,ddl='varchar(200)')
	primary_dbtablecolumn_colid = StringField(ddl='varchar(200)')
	slave_dbtablecolumn_colid = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	primary_tabid = StringField(ddl='varchar(200)')
	slave_tabid = StringField(ddl='varchar(200)')


class V_DBTABLECOLUMN(Model):
	__table__ = 'v_dbtablecolumn'

	id = StringField(primary_key=True,ddl='varchar(200)')
	colid = StringField(ddl='varchar(200)')
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

	id = StringField(primary_key=True,ddl='varchar(200)')
	colid = StringField(ddl='varchar(200)')
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

	id = StringField(primary_key=True,ddl='varchar(200)')
	colid = StringField(ddl='varchar(200)')
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
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')


class V_DBTABLETREE(Model):
	__table__ = 'v_dbtabletree'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')


class V_DC_GROUP(Model):
	__table__ = 'v_dc_group'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	effect = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class V_DC_SCRIPT_DEVELOPMENT(Model):
	__table__ = 'v_dc_script_development'

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
	username = StringField(ddl='varchar(200)')


class V_DC_SCRIPT_JOIN_GROUP(Model):
	__table__ = 'v_dc_script_join_group'

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
	group_name = StringField(ddl='varchar(200)')
	group_type = StringField(ddl='varchar(200)')
	group_effect = StringField(ddl='varchar(200)')
	group_remark = StringField(ddl='varchar(200)')


class V_DI_MODEL(Model):
	__table__ = 'v_di_model'

	id = StringField(primary_key=True,ddl='varchar(200)')
	data_connect_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	datalayer = StringField(ddl='varchar(200)')
	table_num = StringField(ddl='varchar(200)')
	data_volume = StringField(ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class V_EX_BRIDGE_INFO(Model):
	__table__ = 'v_ex_bridge_info'

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


class V_EX_JHQJGL(Model):
	__table__ = 'v_ex_jhqjgl'

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


class V_EX_SJYGL(Model):
	__table__ = 'v_ex_sjygl'

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
	node_name = StringField(ddl='varchar(200)')
	realm_name = StringField(ddl='varchar(200)')


class V_GET_DATA(Model):
	__table__ = 'v_get_data'

	id = StringField(primary_key=True,ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	start_time = StringField(ddl='varchar(200)')
	end_time = StringField(ddl='varchar(200)')
	table_name = StringField(ddl='varchar(200)')
	account_id = StringField(ddl='varchar(200)')
	column_map = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	service_name = StringField(ddl='varchar(200)')
	ip = StringField(ddl='varchar(200)')
	port = StringField(ddl='varchar(200)')
	account = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')
	base_name = StringField(ddl='varchar(200)')
	coding = StringField(ddl='varchar(200)')
	v_remark = StringField(ddl='varchar(200)')


class V_IC_JOB(Model):
	__table__ = 'v_ic_job'

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
	hostip = StringField(ddl='varchar(200)')
	cpu = StringField(ddl='varchar(200)')
	memory = StringField(ddl='varchar(200)')
	harddisk = StringField(ddl='varchar(200)')
	other = StringField(ddl='varchar(200)')


class V_IC_RESOURCE(Model):
	__table__ = 'v_ic_resource'

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


class V_IC_RESOURCE_GROUP(Model):
	__table__ = 'v_ic_resource_group'

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


class V_IC_SOURCE_DATABASE(Model):
	__table__ = 'v_ic_source_database'

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


class V_IC_SOURCE_DATABASE_TABLE(Model):
	__table__ = 'v_ic_source_database_table'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	ic_source_database_id = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class V_IC_SOURCE_DATABASE_TABLE_COLUMN(Model):
	__table__ = 'v_ic_source_database_table_column'

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


class V_JSONTABLESTRUCTARRAY(Model):
	__table__ = 'v_jsontablestructarray'

	id = StringField(primary_key=True,ddl='varchar(200)')
	rn = StringField(ddl='varchar(200)')
	tablestructarray = StringField(ddl='varchar(200)')


class V_MC_DATA_STANDARD(Model):
	__table__ = 'v_mc_data_standard'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	filepath = StringField(ddl='varchar(200)')
	createusername = StringField(ddl='varchar(200)')
	updateusername = StringField(ddl='varchar(200)')


class V_METADATA(Model):
	__table__ = 'v_metadata'

	id = StringField(primary_key=True,ddl='varchar(200)')
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
	metaid = StringField(ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')


class V_METADATACLASS(Model):
	__table__ = 'v_metadataclass'

	id = StringField(primary_key=True,ddl='varchar(200)')
	metaclsname = StringField(ddl='varchar(200)')
	metaclsno = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')
	metaclspy = StringField(ddl='varchar(200)')
	createname = StringField(ddl='varchar(200)')
	app = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	dbtable = StringField(ddl='varchar(200)')
	olddbtable = StringField(ddl='varchar(200)')
	mcid = StringField(ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')


class V_METADATATREE(Model):
	__table__ = 'v_metadatatree'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	columnname = StringField(ddl='varchar(200)')
	columntype = StringField(ddl='varchar(200)')
	columnlen = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')


class V_MN_JOIN_SCRIPT_LOG_JOIN_DBTABLE_JOIN_SCRIPT_DEV(Model):
	__table__ = 'v_mn_join_script_log_join_dbtable_join_script_dev'

	id = StringField(primary_key=True,ddl='varchar(200)')
	dc_script_run_log_id = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	dc_script_development_id = StringField(ddl='varchar(200)')
	begintime = StringField(ddl='varchar(200)')
	endtime = StringField(ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	dlid = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class V_MN_JOIN_SEC_GROUP_JOIN_DBTABLE(Model):
	__table__ = 'v_mn_join_sec_group_join_dbtable'

	id = StringField(primary_key=True,ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	sec_group_id = StringField(ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	dlid = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	groupname = StringField(ddl='varchar(200)')
	groupremark = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_USERS_JOIN_DBTABLE(Model):
	__table__ = 'v_mn_join_sys_users_join_dbtable'

	id = StringField(primary_key=True,ddl='varchar(200)')
	sys_users_id = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	sex = StringField(ddl='varchar(200)')
	job = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	account_id = StringField(ddl='varchar(200)')
	tabid = StringField(ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	dlid = StringField(ddl='varchar(200)')
	resname = StringField(ddl='varchar(200)')
	dlname = StringField(ddl='varchar(200)')
	shortname = StringField(ddl='varchar(200)')
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')


class V_NODE_INFO(Model):
	__table__ = 'v_node_info'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class V_READY_APPLY_RESOURCE(Model):
	__table__ = 'v_ready_apply_resource'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_code = StringField(ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	service_name = StringField(ddl='varchar(200)')
	apply_title = StringField(ddl='varchar(200)')
	apply_type = StringField(ddl='varchar(200)')
	applicant = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	service_status = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')


class V_REALM_INFO(Model):
	__table__ = 'v_realm_info'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class V_RESOURCE_APPLY(Model):
	__table__ = 'v_resource_apply'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_code = StringField(ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	service_name = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	data_realm = StringField(ddl='varchar(200)')
	serivce_type = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	release_time = StringField(ddl='varchar(200)')
	service_status = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	apply_status = StringField(ddl='varchar(200)')


class V_RESOURCE_AUDITOR(Model):
	__table__ = 'v_resource_auditor'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	cam_user_id = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')
	create_user_name = StringField(ddl='varchar(200)')
	update_user_name = StringField(ddl='varchar(200)')
	auditor_name = StringField(ddl='varchar(200)')


class V_RESOURCE_CLASS(Model):
	__table__ = 'v_resource_class'

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
	pid = StringField(ddl='varchar(200)')


class V_RESOURCE_CLASS_TREE(Model):
	__table__ = 'v_resource_class_tree'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	level = StringField(ddl='varchar(200)')
	isresource = StringField(ddl='varchar(200)')


class V_RESOURCE_COLUMN(Model):
	__table__ = 'v_resource_column'

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


class V_RESOURCE_DATABASE(Model):
	__table__ = 'v_resource_database'

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


class V_RESOURCE_INFO(Model):
	__table__ = 'v_resource_info'

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


class V_RESOURCE_INFO_CHANGE_REQUEST(Model):
	__table__ = 'v_resource_info_change_request'

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


class V_RESOURCE_INFO_CHANGE_TMP(Model):
	__table__ = 'v_resource_info_change_tmp'

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


class V_RESOURCE_INFO_DEL(Model):
	__table__ = 'v_resource_info_del'

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


class V_RESOURCE_INFO_HAS_RESOURCE_TABLE(Model):
	__table__ = 'v_resource_info_has_resource_table'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_table_id = StringField(ddl='varchar(200)')
	resource_info_id = StringField(ddl='varchar(200)')


class V_RESOURCE_REGISTER(Model):
	__table__ = 'v_resource_register'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	db_name = StringField(ddl='varchar(200)')
	db_coding = StringField(ddl='varchar(200)')
	db_service_name = StringField(ddl='varchar(200)')
	db_ip = StringField(ddl='varchar(200)')
	db_type = StringField(ddl='varchar(200)')
	db_account = StringField(ddl='varchar(200)')
	db_status = StringField(ddl='varchar(200)')
	tab_num = StringField(ddl='varchar(200)')


class V_RESOURCE_RELATION(Model):
	__table__ = 'v_resource_relation'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_code = StringField(ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	resource_type = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	gl_status = StringField(ddl='varchar(200)')
	version = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	update_cycle = StringField(ddl='varchar(200)')


class V_RESOURCE_TABLE(Model):
	__table__ = 'v_resource_table'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	resource_database_id = StringField(ddl='varchar(200)')


class V_RESOURCEBASE(Model):
	__table__ = 'v_resourcebase'

	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	rbid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	datasourceunit = StringField(ddl='varchar(200)')
	createunit = StringField(ddl='varchar(200)')
	contact = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	status = StringField(ddl='varchar(200)')


class V_ROUTER_INFO(Model):
	__table__ = 'v_router_info'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	realm_info_id = StringField(ddl='varchar(200)')


class V_SC_APPLICATION_RECORD(Model):
	__table__ = 'v_sc_application_record'

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
	tablenameyw = StringField(ddl='varchar(200)')
	tablenamezw = StringField(ddl='varchar(200)')


class V_SC_GROUP(Model):
	__table__ = 'v_sc_group'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	groupname = StringField(ddl='varchar(200)')
	appname = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class V_SC_LOG(Model):
	__table__ = 'v_sc_log'

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


class V_SC_SERVICE(Model):
	__table__ = 'v_sc_service'

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


class V_SC_SERVICE_JOIN_GROUP(Model):
	__table__ = 'v_sc_service_join_group'

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
	groupname = StringField(ddl='varchar(200)')
	appname = StringField(ddl='varchar(200)')
	department = StringField(ddl='varchar(200)')


class V_SC_SERVICE_JOIN_LOG(Model):
	__table__ = 'v_sc_service_join_log'

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
	service_name = StringField(ddl='varchar(200)')
	service_type = StringField(ddl='varchar(200)')
	service_remark = StringField(ddl='varchar(200)')


class V_SC_SERVICE_REQUEST_PARAMETERS(Model):
	__table__ = 'v_sc_service_request_parameters'

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


class V_SEC_GROUP(Model):
	__table__ = 'v_sec_group'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')


class V_SERVICE_APPLY_INFO(Model):
	__table__ = 'v_service_apply_info'

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


class V_SERVICE_REGISTER(Model):
	__table__ = 'v_service_register'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_code = StringField(ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	resource_type = StringField(ddl='varchar(200)')
	share_type = StringField(ddl='varchar(200)')
	share_mode = StringField(ddl='varchar(200)')
	gl_status = StringField(ddl='varchar(200)')
	version = StringField(ddl='varchar(200)')
	provider = StringField(ddl='varchar(200)')
	resource_class_id = StringField(ddl='varchar(200)')
	service_register_id = StringField(ddl='varchar(200)')
	srv_reg_status = StringField(ddl='varchar(200)')


class V_SERVICE_REGISTER_INFO(Model):
	__table__ = 'v_service_register_info'

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


class V_SYS_DICT(Model):
	__table__ = 'v_sys_dict'

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


class V_SYS_USERS(Model):
	__table__ = 'v_sys_users'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	account_id = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	sex = StringField(ddl='varchar(200)')
	job = StringField(ddl='varchar(200)')
	tel = StringField(ddl='varchar(200)')
	email = StringField(ddl='varchar(200)')
	sso_subid = StringField(ddl='varchar(200)')
	file_path = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	remark = StringField(ddl='varchar(200)')
	password = StringField(ddl='varchar(200)')


class V_SYS_USERS_HAS_DBTABLE(Model):
	__table__ = 'v_sys_users_has_dbtable'

	id = StringField(primary_key=True,ddl='varchar(200)')
	sys_users_id = StringField(ddl='varchar(200)')
	dbtable_tabid = StringField(ddl='varchar(200)')


class V_SYS_USERS_HAS_SEC_GROUP(Model):
	__table__ = 'v_sys_users_has_sec_group'

	id = StringField(primary_key=True,ddl='varchar(200)')
	sys_users_id = StringField(ddl='varchar(200)')
	sec_group_id = StringField(ddl='varchar(200)')
	expiredata = StringField(ddl='varchar(200)')


class V_TAG_INFO(Model):
	__table__ = 'v_tag_info'

	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	code = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class V_TASK_HOST_INFO(Model):
	__table__ = 'v_task_host_info'

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


class V_TASK_INFO(Model):
	__table__ = 'v_task_info'

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


class V_TODO(Model):
	__table__ = 'v_todo'

	id = StringField(primary_key=True,ddl='varchar(200)')
	resource_name = StringField(ddl='varchar(200)')
	submit_department = StringField(ddl='varchar(200)')
	submit_person = StringField(ddl='varchar(200)')
	yw_type = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	audit_status = StringField(ddl='varchar(200)')
	viewdesc = StringField(ddl='varchar(200)')


class V_TREE_DATALIST(Model):
	__table__ = 'v_tree_datalist'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


class V_TREE_RESOURCEBASE(Model):
	__table__ = 'v_tree_resourcebase'
	__tree__ =  True
	id = StringField(primary_key=True,ddl='varchar(200)')
	pid = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')


