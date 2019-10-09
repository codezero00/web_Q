import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *


async def SYS_ACTION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_ACTION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                name:
                  type: string
                value:
                  type: string
                menu_id:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_ACTION(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            name=n.get('name'),
            value=n.get('value'),
            menu_id=n.get('menu_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_DICT_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_DICT批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_DICT(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            code=n.get('code'),
            name=n.get('name'),
            level=n.get('level'),
            remark=n.get('remark'),
            sort=n.get('sort'),
            pid=n.get('pid'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ELEMENT_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_ELEMENT批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                name:
                  type: string
                value:
                  type: string
                menu_id:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_ELEMENT(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            name=n.get('name'),
            value=n.get('value'),
            menu_id=n.get('menu_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_FILE_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_FILE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_FILE(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_MENU_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_MENU批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_MENU(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            namezh=n.get('namezh'),
            name=n.get('name'),
            path=n.get('path'),
            component=n.get('component'),
            title=n.get('title'),
            icon=n.get('icon'),
            level=n.get('level'),
            pid=n.get('pid'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ORGANIZATION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_ORGANIZATION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_ORGANIZATION(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            code=n.get('code'),
            name=n.get('name'),
            fullname=n.get('fullname'),
            location=n.get('location'),
            x=n.get('x'),
            y=n.get('y'),
            remark=n.get('remark'),
            isvalid=n.get('isvalid'),
            pid=n.get('pid'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                type:
                  type: string
                remark:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_PERMISSION(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            type=n.get('type'),
            remark=n.get('remark'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ACTION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ACTION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_PERMISSION_HAS_SYS_ACTION(id=next_id(),
            sys_permission_id=n.get('sys_permission_id'),
            sys_action_id=n.get('sys_action_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ELEMENT_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ELEMENT批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_PERMISSION_HAS_SYS_ELEMENT(id=next_id(),
            sys_permission_id=n.get('sys_permission_id'),
            sys_element_id=n.get('sys_element_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_FILE_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_FILE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_PERMISSION_HAS_SYS_FILE(id=next_id(),
            sys_permission_id=n.get('sys_permission_id'),
            sys_file_id=n.get('sys_file_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_MENU_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_MENU批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_PERMISSION_HAS_SYS_MENU(id=next_id(),
            sys_permission_id=n.get('sys_permission_id'),
            sys_menu_id=n.get('sys_menu_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_ROLES批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                name:
                  type: string
                code:
                  type: string
                remark:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_ROLES(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            name=n.get('name'),
            code=n.get('code'),
            remark=n.get('remark'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_HAS_SYS_PERMISSION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_ROLES_HAS_SYS_PERMISSION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_ROLES_HAS_SYS_PERMISSION(id=next_id(),
            sys_roles_id=n.get('sys_roles_id'),
            sys_permission_id=n.get('sys_permission_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                pid:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
                  type: string
                code:
                  type: string
                name:
                  type: string
                remark:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USER_GROUP(id=next_id(),
            pid=n.get('pid'),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            code=n.get('code'),
            name=n.get('name'),
            remark=n.get('remark'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_HAS_SYS_ROLES_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP_HAS_SYS_ROLES批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USER_GROUP_HAS_SYS_ROLES(id=next_id(),
            sys_user_group_id=n.get('sys_user_group_id'),
            sys_roles_id=n.get('sys_roles_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USERS批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
              type: object
              properties:
                id:
                  type: string
                createuserid:
                  type: string
                createtime:
                  type: string
                updateuserid:
                  type: string
                updatetime:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USERS(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            name=n.get('name'),
            sex=n.get('sex'),
            job=n.get('job'),
            tel=n.get('tel'),
            account=n.get('account'),
            expiredtime=n.get('expiredtime'),
            oauth2_id=n.get('oauth2_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ORGANIZATION_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ORGANIZATION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USERS_HAS_SYS_ORGANIZATION(id=next_id(),
            sys_users_id=n.get('sys_users_id'),
            sys_organization_id=n.get('sys_organization_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ROLES_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ROLES批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USERS_HAS_SYS_ROLES(id=next_id(),
            sys_users_id=n.get('sys_users_id'),
            sys_roles_id=n.get('sys_roles_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_USER_GROUP_BatchIns(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_USER_GROUP批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SYS_USERS_HAS_SYS_USER_GROUP(id=next_id(),
            sys_users_id=n.get('sys_users_id'),
            sys_user_group_id=n.get('sys_user_group_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

