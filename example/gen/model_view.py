import time
import uuid
from webQ.q_orm import *


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION(Model):
    __table__ = 'v_mn_join_sys_permission_join_sys_action'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_action_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT(Model):
    __table__ = 'v_mn_join_sys_permission_join_sys_element'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_element_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU(Model):
    __table__ = 'v_mn_join_sys_permission_join_sys_menu'
    sys_permission_id = StringField(ddl='varchar(200)')
    sys_menu_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    namezh = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    path = StringField(ddl='varchar(200)')
    component = StringField(ddl='varchar(200)')
    title = StringField(ddl='varchar(200)')
    icon = StringField(ddl='varchar(200)')
    level = StringField(ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION(Model):
    __table__ = 'v_mn_join_sys_roles_join_sys_permission'
    sys_roles_id = StringField(ddl='varchar(200)')
    sys_permission_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    roles_remark = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    permission_remark = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION(Model):
    __table__ = 'v_mn_join_sys_users_join_sys_organization'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_organization_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    sex = StringField(ddl='varchar(200)')
    job = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    account = StringField(ddl='varchar(200)')
    expiredtime = StringField(ddl='varchar(200)')
    oauth2_id = StringField(ddl='varchar(200)')
    organization_name = StringField(ddl='varchar(200)')
    organization_fullname = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    location = StringField(ddl='varchar(200)')
    x = StringField(ddl='varchar(200)')
    y = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')
    isvalid = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES(Model):
    __table__ = 'v_mn_join_sys_users_join_sys_roles'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_roles_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    sex = StringField(ddl='varchar(200)')
    job = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    account = StringField(ddl='varchar(200)')
    expiredtime = StringField(ddl='varchar(200)')
    oauth2_id = StringField(ddl='varchar(200)')
    roles_name = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')


class V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP(Model):
    __table__ = 'v_mn_join_sys_users_join_sys_user_group'
    sys_users_id = StringField(ddl='varchar(200)')
    sys_organization_id = StringField(ddl='varchar(200)')
    id = StringField(primary_key=True, ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    sex = StringField(ddl='varchar(200)')
    job = StringField(ddl='varchar(200)')
    tel = StringField(ddl='varchar(200)')
    account = StringField(ddl='varchar(200)')
    expiredtime = StringField(ddl='varchar(200)')
    oauth2_id = StringField(ddl='varchar(200)')
    group_name = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    group_remark = StringField(ddl='varchar(200)')


class V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION(Model):
    __table__ = 'v_multijoin_users_roles_permission_menu_element_action'
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
    roles_id = StringField(ddl='varchar(200)')
    roles_name = StringField(ddl='varchar(200)')
    roles_code = StringField(ddl='varchar(200)')
    permission_id = StringField(ddl='varchar(200)')
    permission_type = StringField(ddl='varchar(200)')
    permission_remark = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')
    menu_namezh = StringField(ddl='varchar(200)')
    menu_name = StringField(ddl='varchar(200)')
    menu_path = StringField(ddl='varchar(200)')
    menu_component = StringField(ddl='varchar(200)')
    menu_title = StringField(ddl='varchar(200)')
    menu_icon = StringField(ddl='varchar(200)')
    menu_level = StringField(ddl='varchar(200)')
    element_id = StringField(ddl='varchar(200)')
    element_name = StringField(ddl='varchar(200)')
    element_value = StringField(ddl='varchar(200)')
    action_name = StringField(ddl='varchar(200)')
    action_value = StringField(ddl='varchar(200)')


class V_SYS_ACTION(Model):
    __table__ = 'v_sys_action'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class V_SYS_DICT(Model):
    __table__ = 'v_sys_dict'
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


class V_SYS_ELEMENT(Model):
    __table__ = 'v_sys_element'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    value = StringField(ddl='varchar(200)')
    menu_id = StringField(ddl='varchar(200)')


class V_SYS_MENU(Model):
    __table__ = 'v_sys_menu'
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


class V_SYS_ORGANIZATION(Model):
    __table__ = 'v_sys_organization'
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


class V_SYS_PERMISSION(Model):
    __table__ = 'v_sys_permission'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    type = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class V_SYS_ROLES(Model):
    __table__ = 'v_sys_roles'
    id = StringField(primary_key=True, ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class V_SYS_USER_GROUP(Model):
    __table__ = 'v_sys_user_group'
    id = StringField(primary_key=True, ddl='varchar(200)')
    pid = StringField(ddl='varchar(200)')
    createuserid = StringField(ddl='varchar(200)')
    createtime = StringField(ddl='varchar(200)')
    updateuserid = StringField(ddl='varchar(200)')
    updatetime = StringField(ddl='varchar(200)')
    code = StringField(ddl='varchar(200)')
    name = StringField(ddl='varchar(200)')
    remark = StringField(ddl='varchar(200)')


class V_SYS_USERS(Model):
    __table__ = 'v_sys_users'
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
