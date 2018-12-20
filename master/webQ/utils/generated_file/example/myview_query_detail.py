import json, time, hashlib, logging
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_helpers import Page



async def V_BLOODEDGE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_BLOODEDGE明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: srcid
      in: query
      type: string
      required: true
      description: srcid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_BLOODEDGE.findAll()
        else:
            tablelist = await V_BLOODEDGE.findAll(where=f'srcid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_BLOODRELATION_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_BLOODRELATION明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: beid
      in: query
      type: string
      required: true
      description: beid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_BLOODRELATION.findAll()
        else:
            tablelist = await V_BLOODRELATION.findAll(where=f'beid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_BLOODVERTEX_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_BLOODVERTEX明细查询
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
            tablelist = await V_BLOODVERTEX.findAll()
        else:
            tablelist = await V_BLOODVERTEX.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DATALAYER_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DATALAYER明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: dlid
      in: query
      type: string
      required: true
      description: dlid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_DATALAYER.findAll()
        else:
            tablelist = await V_DATALAYER.findAll(where=f'dlid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLE明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: tabid
      in: query
      type: string
      required: true
      description: tabid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_DBTABLE.findAll()
        else:
            tablelist = await V_DBTABLE.findAll(where=f'tabid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: colid
      in: query
      type: string
      required: true
      description: colid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_DBTABLECOLUMN.findAll()
        else:
            tablelist = await V_DBTABLECOLUMN.findAll(where=f'colid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN2_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN2明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: colid
      in: query
      type: string
      required: true
      description: colid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_DBTABLECOLUMN2.findAll()
        else:
            tablelist = await V_DBTABLECOLUMN2.findAll(where=f'colid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMN3_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMN3明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: colid
      in: query
      type: string
      required: true
      description: colid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_DBTABLECOLUMN3.findAll()
        else:
            tablelist = await V_DBTABLECOLUMN3.findAll(where=f'colid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLECOLUMNTREE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLECOLUMNTREE明细查询
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
            tablelist = await V_DBTABLECOLUMNTREE.findAll()
        else:
            tablelist = await V_DBTABLECOLUMNTREE.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLELAYERTREE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLELAYERTREE明细查询
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
            tablelist = await V_DBTABLELAYERTREE.findAll()
        else:
            tablelist = await V_DBTABLELAYERTREE.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLETREE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_DBTABLETREE明细查询
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
            tablelist = await V_DBTABLETREE.findAll()
        else:
            tablelist = await V_DBTABLETREE.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_FRONTBASE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_FRONTBASE明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: fbid
      in: query
      type: string
      required: true
      description: fbid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_FRONTBASE.findAll()
        else:
            tablelist = await V_FRONTBASE.findAll(where=f'fbid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_JSONTABLESTRUCTARRAY_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_JSONTABLESTRUCTARRAY明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: rn
      in: query
      type: string
      required: true
      description: rn 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_JSONTABLESTRUCTARRAY.findAll()
        else:
            tablelist = await V_JSONTABLESTRUCTARRAY.findAll(where=f'rn = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATA_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_METADATA明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: metaid
      in: query
      type: string
      required: true
      description: metaid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_METADATA.findAll()
        else:
            tablelist = await V_METADATA.findAll(where=f'metaid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATACLASS_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_METADATACLASS明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: mcid
      in: query
      type: string
      required: true
      description: mcid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_METADATACLASS.findAll()
        else:
            tablelist = await V_METADATACLASS.findAll(where=f'mcid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATATREE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_METADATATREE明细查询
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
            tablelist = await V_METADATATREE.findAll()
        else:
            tablelist = await V_METADATATREE.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_NOSQLBASE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_NOSQLBASE明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: ndid
      in: query
      type: string
      required: true
      description: ndid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_NOSQLBASE.findAll()
        else:
            tablelist = await V_NOSQLBASE.findAll(where=f'ndid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_NOSQLBASETREE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_NOSQLBASETREE明细查询
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
            tablelist = await V_NOSQLBASETREE.findAll()
        else:
            tablelist = await V_NOSQLBASETREE.findAll(where=f'id = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_RESOURCEBASE_Query_Detail(request):
    """
    Description end-point
    ---
    description: V_RESOURCEBASE明细查询
    tags:
    - select detail
    produces:
    - application/json
    parameters:
    - name: rbid
      in: query
      type: string
      required: true
      description: rbid 唯一标示符
    """
    id = request.query.get('id')
    try:
        if not id:
            tablelist = await V_RESOURCEBASE.findAll()
        else:
            tablelist = await V_RESOURCEBASE.findAll(where=f'rbid = "{id}"')
        data = dict(success=True, data=tablelist)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)

