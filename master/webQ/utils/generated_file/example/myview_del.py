import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *
from utils import parestree, parescolumntree, parescasetypetree
import re



async def BLOODEDGE_BatchDel(request):
    """
    Description end-point
    ---
    description: BLOODEDGE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: BLOODEDGE批量删除
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
        sql = f'delete from BLOODEDGE where beid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DATALAYER_BatchDel(request):
    """
    Description end-point
    ---
    description: DATALAYER批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DATALAYER批量删除
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
        sql = f'delete from DATALAYER where dlid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLE_BatchDel(request):
    """
    Description end-point
    ---
    description: DBTABLE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLE批量删除
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
        sql = f'delete from DBTABLE where tabid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLE_RELATION_BatchDel(request):
    """
    Description end-point
    ---
    description: DBTABLE_RELATION批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLE_RELATION批量删除
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
        sql = f'delete from DBTABLE_RELATION where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLECOLUMN_BatchDel(request):
    """
    Description end-point
    ---
    description: DBTABLECOLUMN批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLECOLUMN批量删除
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
        sql = f'delete from DBTABLECOLUMN where colid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def FRONTBASE_BatchDel(request):
    """
    Description end-point
    ---
    description: FRONTBASE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: FRONTBASE批量删除
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
        sql = f'delete from FRONTBASE where fbid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_JOB_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_JOB批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_JOB批量删除
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
        sql = f'delete from IC_JOB where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_RESOURCE_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_RESOURCE批量删除
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
        sql = f'delete from IC_RESOURCE where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_RESOURCE_GROUP_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE_GROUP批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_RESOURCE_GROUP批量删除
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
        sql = f'delete from IC_RESOURCE_GROUP where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE批量删除
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
        sql = f'delete from IC_SOURCE_DATABASE where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_TABLE_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE_TABLE批量删除
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
        sql = f'delete from IC_SOURCE_DATABASE_TABLE where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_TABLE_COLUMN_BatchDel(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE_COLUMN批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE_TABLE_COLUMN批量删除
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
        sql = f'delete from IC_SOURCE_DATABASE_TABLE_COLUMN where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def METADATA_BatchDel(request):
    """
    Description end-point
    ---
    description: METADATA批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: METADATA批量删除
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
        sql = f'delete from METADATA where metaid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def METADATACLASS_BatchDel(request):
    """
    Description end-point
    ---
    description: METADATACLASS批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: METADATACLASS批量删除
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
        sql = f'delete from METADATACLASS where mcid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def NOSQLBASE_BatchDel(request):
    """
    Description end-point
    ---
    description: NOSQLBASE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: NOSQLBASE批量删除
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
        sql = f'delete from NOSQLBASE where ndid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def RESOURCEBASE_BatchDel(request):
    """
    Description end-point
    ---
    description: RESOURCEBASE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: RESOURCEBASE批量删除
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
        sql = f'delete from RESOURCEBASE where rbid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_APPLICATION_RECORD_BatchDel(request):
    """
    Description end-point
    ---
    description: SC_APPLICATION_RECORD批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_APPLICATION_RECORD批量删除
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
        sql = f'delete from SC_APPLICATION_RECORD where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_GROUP_BatchDel(request):
    """
    Description end-point
    ---
    description: SC_GROUP批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_GROUP批量删除
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
        sql = f'delete from SC_GROUP where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_LOG_BatchDel(request):
    """
    Description end-point
    ---
    description: SC_LOG批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_LOG批量删除
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
        sql = f'delete from SC_LOG where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_SERVICE_BatchDel(request):
    """
    Description end-point
    ---
    description: SC_SERVICE批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_SERVICE批量删除
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
        sql = f'delete from SC_SERVICE where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_SERVICE_REQUEST_PARAMETERS_BatchDel(request):
    """
    Description end-point
    ---
    description: SC_SERVICE_REQUEST_PARAMETERS批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_SERVICE_REQUEST_PARAMETERS批量删除
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
        sql = f'delete from SC_SERVICE_REQUEST_PARAMETERS where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def USERS_BatchDel(request):
    """
    Description end-point
    ---
    description: USERS批量删除
    tags:
    - batch delete
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: USERS批量删除
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
        sql = f'delete from USERS where id in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

