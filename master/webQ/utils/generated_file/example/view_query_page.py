import json, time, hashlib, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_helpers import Page
from model_view import *


async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ACTION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_ELEMENT.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_PERMISSION_JOIN_SYS_MENU.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_ROLES_JOIN_SYS_PERMISSION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ORGANIZATION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_USERS_JOIN_SYS_ROLES.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MN_JOIN_SYS_USERS_JOIN_SYS_USER_GROUP.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_MULTIJOIN_USERS_ROLES_PERMISSION_MENU_ELEMENT_ACTION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ACTION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_ACTION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_ACTION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_ACTION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_DICT_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_DICT分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_DICT.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_DICT.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ELEMENT_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_ELEMENT分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_ELEMENT.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_ELEMENT.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_MENU_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_MENU分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_MENU.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_MENU.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ORGANIZATION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_ORGANIZATION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_ORGANIZATION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_ORGANIZATION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_PERMISSION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_PERMISSION分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_PERMISSION.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_PERMISSION.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_ROLES_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_ROLES分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_ROLES.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_ROLES.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_USER_GROUP_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_USER_GROUP分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_USER_GROUP.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_USER_GROUP.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_SYS_USERS_Query_Page(request):
    """
    Description end-point
    ---
    description: V_SYS_USERS分页查询
    tags:
    - select page
    produces:
    - application/json
    parameters:
    - name: CurrentPage
      in: query
      type: string
      required: true
      description: 当前页
    - name: PageSize
      in: query
      type: string
      required: true
      description: 每一页条数
    - name: Where
      in: query
      type: string
      description: where条件
    - name: OrderBy
      in: query
      type: string
      description: 排序
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    Where = request.query.get('Where')
    OrderBy = request.query.get('OrderBy')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_SYS_USERS.findNumber(selectField='count(*)',where=Where)
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_SYS_USERS.findAll(selectField='*',where=Where,orderBy=OrderBy, limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)

