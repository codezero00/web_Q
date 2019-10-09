import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *
from utils import parestree, parescolumntree, parescasetypetree


async def SYS_ACTION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_ACTION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ACTION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          name:
            type: string
          value:
            type: string
          menu_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    name = form.get('name')
    value = form.get('value')
    menu_id = form.get('menu_id')

    try:
        if id:  # update
            effectrows = await SYS_ACTION(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            value=value,
            menu_id=menu_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_ACTION().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            value=value,
            menu_id=menu_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_DICT_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_DICT插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_DICT插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          code:
            type: string
          name:
            type: string
          level:
            type: string
          remark:
            type: string
          sort:
            type: string
          pid:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    code = form.get('code')
    name = form.get('name')
    level = form.get('level')
    remark = form.get('remark')
    sort = form.get('sort')
    pid = form.get('pid')

    try:
        if id:  # update
            effectrows = await SYS_DICT(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            level=level,
            remark=remark,
            sort=sort,
            pid=pid,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_DICT().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            level=level,
            remark=remark,
            sort=sort,
            pid=pid,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ELEMENT_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_ELEMENT插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ELEMENT插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          name:
            type: string
          value:
            type: string
          menu_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    name = form.get('name')
    value = form.get('value')
    menu_id = form.get('menu_id')

    try:
        if id:  # update
            effectrows = await SYS_ELEMENT(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            value=value,
            menu_id=menu_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_ELEMENT().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            value=value,
            menu_id=menu_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_FILE_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_FILE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_FILE插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')

    try:
        if id:  # update
            effectrows = await SYS_FILE(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_FILE().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_MENU_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_MENU插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_MENU插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          namezh:
            type: string
          name:
            type: string
          path:
            type: string
          component:
            type: string
          title:
            type: string
          icon:
            type: string
          level:
            type: string
          pid:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    namezh = form.get('namezh')
    name = form.get('name')
    path = form.get('path')
    component = form.get('component')
    title = form.get('title')
    icon = form.get('icon')
    level = form.get('level')
    pid = form.get('pid')

    try:
        if id:  # update
            effectrows = await SYS_MENU(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            namezh=namezh,
            name=name,
            path=path,
            component=component,
            title=title,
            icon=icon,
            level=level,
            pid=pid,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_MENU().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            namezh=namezh,
            name=name,
            path=path,
            component=component,
            title=title,
            icon=icon,
            level=level,
            pid=pid,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ORGANIZATION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_ORGANIZATION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ORGANIZATION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          code:
            type: string
          name:
            type: string
          fullname:
            type: string
          location:
            type: string
          x:
            type: string
          y:
            type: string
          remark:
            type: string
          isvalid:
            type: string
          pid:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    code = form.get('code')
    name = form.get('name')
    fullname = form.get('fullname')
    location = form.get('location')
    x = form.get('x')
    y = form.get('y')
    remark = form.get('remark')
    isvalid = form.get('isvalid')
    pid = form.get('pid')

    try:
        if id:  # update
            effectrows = await SYS_ORGANIZATION(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            fullname=fullname,
            location=location,
            x=x,
            y=y,
            remark=remark,
            isvalid=isvalid,
            pid=pid,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_ORGANIZATION().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            fullname=fullname,
            location=location,
            x=x,
            y=y,
            remark=remark,
            isvalid=isvalid,
            pid=pid,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          type:
            type: string
          remark:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    type = form.get('type')
    remark = form.get('remark')

    try:
        if id:  # update
            effectrows = await SYS_PERMISSION(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            type=type,
            remark=remark,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_PERMISSION().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            type=type,
            remark=remark,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ACTION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ACTION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_ACTION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_permission_id:
            type: string
          sys_action_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_permission_id = form.get('sys_permission_id')
    sys_action_id = form.get('sys_action_id')

    try:
        if id:  # update
            effectrows = await SYS_PERMISSION_HAS_SYS_ACTION(id=id).upd2(sys_permission_id=sys_permission_id,
            sys_action_id=sys_action_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_PERMISSION_HAS_SYS_ACTION().save2(id=id,
            sys_permission_id=sys_permission_id,
            sys_action_id=sys_action_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ELEMENT_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ELEMENT插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_ELEMENT插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_permission_id:
            type: string
          sys_element_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_permission_id = form.get('sys_permission_id')
    sys_element_id = form.get('sys_element_id')

    try:
        if id:  # update
            effectrows = await SYS_PERMISSION_HAS_SYS_ELEMENT(id=id).upd2(sys_permission_id=sys_permission_id,
            sys_element_id=sys_element_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_PERMISSION_HAS_SYS_ELEMENT().save2(id=id,
            sys_permission_id=sys_permission_id,
            sys_element_id=sys_element_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_FILE_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_FILE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_FILE插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_permission_id:
            type: string
          sys_file_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_permission_id = form.get('sys_permission_id')
    sys_file_id = form.get('sys_file_id')

    try:
        if id:  # update
            effectrows = await SYS_PERMISSION_HAS_SYS_FILE(id=id).upd2(sys_permission_id=sys_permission_id,
            sys_file_id=sys_file_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_PERMISSION_HAS_SYS_FILE().save2(id=id,
            sys_permission_id=sys_permission_id,
            sys_file_id=sys_file_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_MENU_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_MENU插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_MENU插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_permission_id:
            type: string
          sys_menu_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_permission_id = form.get('sys_permission_id')
    sys_menu_id = form.get('sys_menu_id')

    try:
        if id:  # update
            effectrows = await SYS_PERMISSION_HAS_SYS_MENU(id=id).upd2(sys_permission_id=sys_permission_id,
            sys_menu_id=sys_menu_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_PERMISSION_HAS_SYS_MENU().save2(id=id,
            sys_permission_id=sys_permission_id,
            sys_menu_id=sys_menu_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_ROLES插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ROLES插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          name:
            type: string
          code:
            type: string
          remark:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    name = form.get('name')
    code = form.get('code')
    remark = form.get('remark')

    try:
        if id:  # update
            effectrows = await SYS_ROLES(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            code=code,
            remark=remark,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_ROLES().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            code=code,
            remark=remark,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_HAS_SYS_PERMISSION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_ROLES_HAS_SYS_PERMISSION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ROLES_HAS_SYS_PERMISSION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_roles_id:
            type: string
          sys_permission_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_roles_id = form.get('sys_roles_id')
    sys_permission_id = form.get('sys_permission_id')

    try:
        if id:  # update
            effectrows = await SYS_ROLES_HAS_SYS_PERMISSION(id=id).upd2(sys_roles_id=sys_roles_id,
            sys_permission_id=sys_permission_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_ROLES_HAS_SYS_PERMISSION().save2(id=id,
            sys_roles_id=sys_roles_id,
            sys_permission_id=sys_permission_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USER_GROUP插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          pid:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          code:
            type: string
          name:
            type: string
          remark:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    pid = form.get('pid')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    code = form.get('code')
    name = form.get('name')
    remark = form.get('remark')

    try:
        if id:  # update
            effectrows = await SYS_USER_GROUP(id=id).upd2(pid=pid,
            createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            remark=remark,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USER_GROUP().save2(id=id,
            pid=pid,
            createuserid=createuserid,
            updateuserid=updateuserid,
            code=code,
            name=name,
            remark=remark,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_HAS_SYS_ROLES_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP_HAS_SYS_ROLES插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USER_GROUP_HAS_SYS_ROLES插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_user_group_id:
            type: string
          sys_roles_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_user_group_id = form.get('sys_user_group_id')
    sys_roles_id = form.get('sys_roles_id')

    try:
        if id:  # update
            effectrows = await SYS_USER_GROUP_HAS_SYS_ROLES(id=id).upd2(sys_user_group_id=sys_user_group_id,
            sys_roles_id=sys_roles_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USER_GROUP_HAS_SYS_ROLES().save2(id=id,
            sys_user_group_id=sys_user_group_id,
            sys_roles_id=sys_roles_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USERS插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          createuserid:
            type: string
          updateuserid:
            type: string
          name:
            type: string
          sex:
            type: string
          job:
            type: string
          tel:
            type: string
          account:
            type: string
          expiredtime:
            type: string
          oauth2_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    name = form.get('name')
    sex = form.get('sex')
    job = form.get('job')
    tel = form.get('tel')
    account = form.get('account')
    expiredtime = form.get('expiredtime')
    oauth2_id = form.get('oauth2_id')

    try:
        if id:  # update
            effectrows = await SYS_USERS(id=id).upd2(createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            sex=sex,
            job=job,
            tel=tel,
            account=account,
            expiredtime=expiredtime,
            oauth2_id=oauth2_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USERS().save2(id=id,
            createuserid=createuserid,
            updateuserid=updateuserid,
            name=name,
            sex=sex,
            job=job,
            tel=tel,
            account=account,
            expiredtime=expiredtime,
            oauth2_id=oauth2_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ORGANIZATION_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ORGANIZATION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_ORGANIZATION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_users_id:
            type: string
          sys_organization_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_users_id = form.get('sys_users_id')
    sys_organization_id = form.get('sys_organization_id')

    try:
        if id:  # update
            effectrows = await SYS_USERS_HAS_SYS_ORGANIZATION(id=id).upd2(sys_users_id=sys_users_id,
            sys_organization_id=sys_organization_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USERS_HAS_SYS_ORGANIZATION().save2(id=id,
            sys_users_id=sys_users_id,
            sys_organization_id=sys_organization_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ROLES_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ROLES插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_ROLES插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_users_id:
            type: string
          sys_roles_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_users_id = form.get('sys_users_id')
    sys_roles_id = form.get('sys_roles_id')

    try:
        if id:  # update
            effectrows = await SYS_USERS_HAS_SYS_ROLES(id=id).upd2(sys_users_id=sys_users_id,
            sys_roles_id=sys_roles_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USERS_HAS_SYS_ROLES().save2(id=id,
            sys_users_id=sys_users_id,
            sys_roles_id=sys_roles_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_USER_GROUP_InsOrUp(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_USER_GROUP插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_USER_GROUP插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          sys_users_id:
            type: string
          sys_user_group_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    sys_users_id = form.get('sys_users_id')
    sys_user_group_id = form.get('sys_user_group_id')

    try:
        if id:  # update
            effectrows = await SYS_USERS_HAS_SYS_USER_GROUP(id=id).upd2(sys_users_id=sys_users_id,
            sys_user_group_id=sys_user_group_id,
            )
        elif not id:  # create
            id = next_id()
            effectrows = await SYS_USERS_HAS_SYS_USER_GROUP().save2(id=id,
            sys_users_id=sys_users_id,
            sys_user_group_id=sys_user_group_id,
            )
        data = dict(success=True, data=(effectrows,id))
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

