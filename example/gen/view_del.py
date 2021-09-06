import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *
from utils import parestree, parescolumntree, parescasetypetree
import re



async def SYS_ACTION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_ACTION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ACTION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_action where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_DICT_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_DICT批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_DICT批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_dict where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ELEMENT_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_ELEMENT批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ELEMENT批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_element where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_FILE_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_FILE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_FILE批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_file where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_MENU_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_MENU批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_MENU批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_menu where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ORGANIZATION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_ORGANIZATION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ORGANIZATION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_organization where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_permission where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ACTION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ACTION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_ACTION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_permission_has_sys_action where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_ELEMENT_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_ELEMENT批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_ELEMENT批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_permission_has_sys_element where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_FILE_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_FILE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_FILE批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_permission_has_sys_file where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_PERMISSION_HAS_SYS_MENU_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_PERMISSION_HAS_SYS_MENU批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_PERMISSION_HAS_SYS_MENU批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_permission_has_sys_menu where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_ROLES批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ROLES批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_roles where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_ROLES_HAS_SYS_PERMISSION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_ROLES_HAS_SYS_PERMISSION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_ROLES_HAS_SYS_PERMISSION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_roles_has_sys_permission where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USER_GROUP批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_user_group where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USER_GROUP_HAS_SYS_ROLES_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USER_GROUP_HAS_SYS_ROLES批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USER_GROUP_HAS_SYS_ROLES批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_user_group_has_sys_roles where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USERS批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_users where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ORGANIZATION_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ORGANIZATION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_ORGANIZATION批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_users_has_sys_organization where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_ROLES_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_ROLES批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_ROLES批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_users_has_sys_roles where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SYS_USERS_HAS_SYS_USER_GROUP_BatchDel(request):
    """
    Description end-point
    ---
    description: SYS_USERS_HAS_SYS_USER_GROUP批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SYS_USERS_HAS_SYS_USER_GROUP批量删除
      required: True
      schema:
        type: object
        properties:
          batchid:
            type: string
            description: ['xxx','xxx','xxx',...]
    """
    form = await request.json()
    batchid = form.get('batchid')
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    try:
        sql = f'delete from sys_users_has_sys_user_group where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

