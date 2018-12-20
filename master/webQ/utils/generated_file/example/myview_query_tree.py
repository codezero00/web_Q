import json, time, hashlib, logging
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_helpers import Page


async def V_DBTABLECOLUMNTREE_Query_Tree(request):
    """
    ---
    description: V_DBTABLECOLUMNTREE树查询！
    tags:
    - select
    produces:
    - application/json
    """
    try:
        treelist = await V_DBTABLECOLUMNTREE.findAll()
        data = dict(success=True, data=parestree(treelist))
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLELAYERTREE_Query_Tree(request):
    """
    ---
    description: V_DBTABLELAYERTREE树查询！
    tags:
    - select
    produces:
    - application/json
    """
    try:
        treelist = await V_DBTABLELAYERTREE.findAll()
        data = dict(success=True, data=parestree(treelist))
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_DBTABLETREE_Query_Tree(request):
    """
    ---
    description: V_DBTABLETREE树查询！
    tags:
    - select
    produces:
    - application/json
    """
    try:
        treelist = await V_DBTABLETREE.findAll()
        data = dict(success=True, data=parestree(treelist))
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_METADATATREE_Query_Tree(request):
    """
    ---
    description: V_METADATATREE树查询！
    tags:
    - select
    produces:
    - application/json
    """
    try:
        treelist = await V_METADATATREE.findAll()
        data = dict(success=True, data=parestree(treelist))
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def V_NOSQLBASETREE_Query_Tree(request):
    """
    ---
    description: V_NOSQLBASETREE树查询！
    tags:
    - select
    produces:
    - application/json
    """
    try:
        treelist = await V_NOSQLBASETREE.findAll()
        data = dict(success=True, data=parestree(treelist))
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)

