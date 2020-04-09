import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class SYS_ACTION(Model):
    __table__ = 'sys_action'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class SYS_DICT(Model):
    __table__ = 'sys_dict'
    id = StringField(primary_key=True, ddl='varchar(200)')
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


class SYS_ELEMENT(Model):
    __table__ = 'sys_element'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class SYS_FILE(Model):
    __table__ = 'sys_file'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')


class SYS_MENU(Model):
    __table__ = 'sys_menu'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    namezh = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    path = StringField(ddl='varchar(200)')
    component = StringField(ddl='varchar(200)')
    title = StringField(ddl='varchar(200)')
    icon = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')


class SYS_ORGANIZATION(Model):
    __table__ = 'sys_organization'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    fullname = StringField(ddl='varchar(200)')
    location = StringField(ddl='varchar(200)')
    x = StringField(ddl='varchar(200)')
    y = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    isvalid = StringField(ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')


class SYS_PERMISSION(Model):
    __table__ = 'sys_permission'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class SYS_PERMISSION_HAS_SYS_ACTION(Model):
    __table__ = 'sys_permission_has_sys_action'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_action_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_PERMISSION_HAS_SYS_ELEMENT(Model):
    __table__ = 'sys_permission_has_sys_element'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_element_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_PERMISSION_HAS_SYS_FILE(Model):
    __table__ = 'sys_permission_has_sys_file'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_file_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_PERMISSION_HAS_SYS_MENU(Model):
    __table__ = 'sys_permission_has_sys_menu'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_menu_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_ROLES(Model):
    __table__ = 'sys_roles'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class SYS_ROLES_HAS_SYS_PERMISSION(Model):
    __table__ = 'sys_roles_has_sys_permission'
    sys_roles_id = StringField(ddl='varchar(200)')
    sys_permission_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_USER_GROUP(Model):
    __table__ = 'sys_user_group'
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class SYS_USER_GROUP_HAS_SYS_ROLES(Model):
    __table__ = 'sys_user_group_has_sys_roles'
    sys_user_group_id = StringField(ddl='varchar(200)')
    sys_roles_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_USERS(Model):
    __table__ = 'sys_users'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    sex = StringField(ddl='varchar(200)')
    job = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    account = StringField(ddl='varchar(200)')
    expiredtime = StringField(ddl='varchar(200)')
    oauth2_id = StringField(ddl='varchar(200)')


class SYS_USERS_HAS_SYS_ORGANIZATION(Model):
    __table__ = 'sys_users_has_sys_organization'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_organization_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_USERS_HAS_SYS_ROLES(Model):
    __table__ = 'sys_users_has_sys_roles'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_roles_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')


class SYS_USERS_HAS_SYS_USER_GROUP(Model):
    __table__ = 'sys_users_has_sys_user_group'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_user_group_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
