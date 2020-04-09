import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class DAILY_COEFFICIENT(Model):
	__table__ = 'daily_coefficient'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	factor = StringField(ddl='varchar(200)')


class EPIDEMIC_COEFFICIENT(Model):
	__table__ = 'epidemic_coefficient'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	factor = StringField(ddl='varchar(200)')


class GOODS_RECEIVE(Model):
	__table__ = 'goods_receive'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	name = StringField(ddl='varchar(200)')
	type = StringField(ddl='varchar(200)')
	num = StringField(ddl='varchar(200)')
	getdate = StringField(ddl='varchar(200)')


class NCP_PATIENTS_ACCEPT(Model):
	__table__ = 'ncp_patients_accept'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	date = StringField(ddl='varchar(200)')
	in_hospital = StringField(ddl='varchar(200)')
	out_hospital = StringField(ddl='varchar(200)')
	patients = StringField(ddl='varchar(200)')
	ncp = StringField(ddl='varchar(200)')


class NCP_PATIENTS_PREDICTION(Model):
	__table__ = 'ncp_patients_prediction'
	id = StringField(primary_key=True,ddl='varchar(200)')
	createuserid = StringField(ddl='varchar(200)')
	createtime = StringField(ddl='varchar(200)')
	updateuserid = StringField(ddl='varchar(200)')
	updatetime = StringField(ddl='varchar(200)')
	date = StringField(ddl='varchar(200)')
	in_hospital = StringField(ddl='varchar(200)')
	ncp = StringField(ddl='varchar(200)')


