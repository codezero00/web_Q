import json, time, hashlib, logging
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_helpers import Page



async def V_BLOODEDGE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_BLOODEDGE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_BLOODEDGE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_BLOODEDGE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_BLOODRELATION_Query_Page(request):
    """
    Description end-point
    ---
    description: V_BLOODRELATION分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_BLOODRELATION.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_BLOODRELATION.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_BLOODVERTEX_Query_Page(request):
    """
    Description end-point
    ---
    description: V_BLOODVERTEX分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_BLOODVERTEX.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_BLOODVERTEX.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DATALAYER_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DATALAYER分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DATALAYER.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DATALAYER.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLECOLUMN.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLECOLUMN.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN2_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN2分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLECOLUMN2.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLECOLUMN2.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN3_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN3分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLECOLUMN3.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLECOLUMN3.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMNTREE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMNTREE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLECOLUMNTREE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLECOLUMNTREE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLELAYERTREE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLELAYERTREE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLELAYERTREE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLELAYERTREE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLETREE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_DBTABLETREE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_DBTABLETREE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_DBTABLETREE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_FRONTBASE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_FRONTBASE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_FRONTBASE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_FRONTBASE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_JSONTABLESTRUCTARRAY_Query_Page(request):
    """
    Description end-point
    ---
    description: V_JSONTABLESTRUCTARRAY分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_JSONTABLESTRUCTARRAY.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_JSONTABLESTRUCTARRAY.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATA_Query_Page(request):
    """
    Description end-point
    ---
    description: V_METADATA分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_METADATA.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_METADATA.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATACLASS_Query_Page(request):
    """
    Description end-point
    ---
    description: V_METADATACLASS分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_METADATACLASS.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_METADATACLASS.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATATREE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_METADATATREE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_METADATATREE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_METADATATREE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_NOSQLBASE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_NOSQLBASE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_NOSQLBASE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_NOSQLBASE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_NOSQLBASETREE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_NOSQLBASETREE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_NOSQLBASETREE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_NOSQLBASETREE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_RESOURCEBASE_Query_Page(request):
    """
    Description end-point
    ---
    description: V_RESOURCEBASE分页查询
    tags:
    - select
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
    """
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await V_RESOURCEBASE.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await V_RESOURCEBASE.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)

