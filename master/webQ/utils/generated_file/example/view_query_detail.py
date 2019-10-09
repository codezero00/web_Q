import json, time, hashlib, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_helpers import Page
from model_view import *



async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP.findAll(selectField='*')
        else:
            tablelist = await V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION.findAll(selectField='*')
        else:
            tablelist = await V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ACTION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_ACTION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_ACTION.findAll(selectField='*')
        else:
            tablelist = await V_SYS_ACTION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_DICT_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_DICT明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_DICT.findAll(selectField='*')
        else:
            tablelist = await V_SYS_DICT.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ELEMENT_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_ELEMENT明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_ELEMENT.findAll(selectField='*')
        else:
            tablelist = await V_SYS_ELEMENT.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_MENU_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_MENU明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_MENU.findAll(selectField='*')
        else:
            tablelist = await V_SYS_MENU.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ORGANIZATION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_ORGANIZATION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_ORGANIZATION.findAll(selectField='*')
        else:
            tablelist = await V_SYS_ORGANIZATION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_PERMISSION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_PERMISSION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_PERMISSION.findAll(selectField='*')
        else:
            tablelist = await V_SYS_PERMISSION.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ROLES_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_ROLES明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_ROLES.findAll(selectField='*')
        else:
            tablelist = await V_SYS_ROLES.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_USER_GROUP_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_USER_GROUP明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_USER_GROUP.findAll(selectField='*')
        else:
            tablelist = await V_SYS_USER_GROUP.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_USERS_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_SYS_USERS明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: id
      in: query
      type: string
      required: true
      description: id 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_SYS_USERS.findAll(selectField='*')
        else:
            tablelist = await V_SYS_USERS.findAll(selectField='*', where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)

