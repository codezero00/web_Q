import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *
from utils import parestree, parescolumntree, parescasetypetree


async def BLOODEDGE_InsOrUp(request):
    """
    Description end-point
    ---
    description: BLOODEDGE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: BLOODEDGE插入/更新
      required: True
      schema:
        type: object
        properties:
          beid:
            type: string
          srcid:
            type: string
          dstid:
            type: string
          relation:
            type: string
          
    """
    form = await request.json()
    id = form.get('beid')
    srcid = form.get('srcid')
    dstid = form.get('dstid')
    relation = form.get('relation')

    try:
        if id:  # update
            effectrows = await BLOODEDGE(beid=id).upd2(srcid=srcid,
            dstid=dstid,
            relation=relation,
            )
        elif not id:  # create
            effectrows = await BLOODEDGE(beid=next_id(),
            srcid=srcid,
            dstid=dstid,
            relation=relation,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DATALAYER_InsOrUp(request):
    """
    Description end-point
    ---
    description: DATALAYER插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DATALAYER插入/更新
      required: True
      schema:
        type: object
        properties:
          dlid:
            type: string
          name:
            type: string
          shortname:
            type: string
          effect:
            type: string
          remark:
            type: string
          status:
            type: string
          sort:
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
    id = form.get('dlid')
    name = form.get('name')
    shortname = form.get('shortname')
    effect = form.get('effect')
    remark = form.get('remark')
    status = form.get('status')
    sort = form.get('sort')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await DATALAYER(dlid=id).upd2(name=name,
            shortname=shortname,
            effect=effect,
            remark=remark,
            status=status,
            sort=sort,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await DATALAYER(dlid=next_id(),
            name=name,
            shortname=shortname,
            effect=effect,
            remark=remark,
            status=status,
            sort=sort,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLE_InsOrUp(request):
    """
    Description end-point
    ---
    description: DBTABLE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLE插入/更新
      required: True
      schema:
        type: object
        properties:
          tabid:
            type: string
          rbid:
            type: string
          dlid:
            type: string
          tablenameyw:
            type: string
          tablenamezw:
            type: string
          remark:
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
    id = form.get('tabid')
    rbid = form.get('rbid')
    dlid = form.get('dlid')
    tablenameyw = form.get('tablenameyw')
    tablenamezw = form.get('tablenamezw')
    remark = form.get('remark')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await DBTABLE(tabid=id).upd2(rbid=rbid,
            dlid=dlid,
            tablenameyw=tablenameyw,
            tablenamezw=tablenamezw,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await DBTABLE(tabid=next_id(),
            rbid=rbid,
            dlid=dlid,
            tablenameyw=tablenameyw,
            tablenamezw=tablenamezw,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLE_RELATION_InsOrUp(request):
    """
    Description end-point
    ---
    description: DBTABLE_RELATION插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLE_RELATION插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          primary_table_id:
            type: string
          slave_talbe_id:
            type: string
          type:
            type: string
          name:
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
    id = form.get('id')
    primary_table_id = form.get('primary_table_id')
    slave_talbe_id = form.get('slave_talbe_id')
    type = form.get('type')
    name = form.get('name')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await DBTABLE_RELATION(id=id).upd2(primary_table_id=primary_table_id,
            slave_talbe_id=slave_talbe_id,
            type=type,
            name=name,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await DBTABLE_RELATION(id=next_id(),
            primary_table_id=primary_table_id,
            slave_talbe_id=slave_talbe_id,
            type=type,
            name=name,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DBTABLECOLUMN_InsOrUp(request):
    """
    Description end-point
    ---
    description: DBTABLECOLUMN插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: DBTABLECOLUMN插入/更新
      required: True
      schema:
        type: object
        properties:
          colid:
            type: string
          tabid:
            type: string
          metaid:
            type: string
          ispk:
            type: string
          isnull:
            type: string
          isuq:
            type: string
          range:
            type: string
          
    """
    form = await request.json()
    id = form.get('colid')
    tabid = form.get('tabid')
    metaid = form.get('metaid')
    ispk = form.get('ispk')
    isnull = form.get('isnull')
    isuq = form.get('isuq')
    range = form.get('range')

    try:
        if id:  # update
            effectrows = await DBTABLECOLUMN(colid=id).upd2(tabid=tabid,
            metaid=metaid,
            ispk=ispk,
            isnull=isnull,
            isuq=isuq,
            range=range,
            )
        elif not id:  # create
            effectrows = await DBTABLECOLUMN(colid=next_id(),
            tabid=tabid,
            metaid=metaid,
            ispk=ispk,
            isnull=isnull,
            isuq=isuq,
            range=range,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def FRONTBASE_InsOrUp(request):
    """
    Description end-point
    ---
    description: FRONTBASE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: FRONTBASE插入/更新
      required: True
      schema:
        type: object
        properties:
          fbid:
            type: string
          name:
            type: string
          ip:
            type: string
          usesoftware:
            type: string
          location:
            type: string
          dept:
            type: string
          effect:
            type: string
          remark:
            type: string
          status:
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
    id = form.get('fbid')
    name = form.get('name')
    ip = form.get('ip')
    usesoftware = form.get('usesoftware')
    location = form.get('location')
    dept = form.get('dept')
    effect = form.get('effect')
    remark = form.get('remark')
    status = form.get('status')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await FRONTBASE(fbid=id).upd2(name=name,
            ip=ip,
            usesoftware=usesoftware,
            location=location,
            dept=dept,
            effect=effect,
            remark=remark,
            status=status,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await FRONTBASE(fbid=next_id(),
            name=name,
            ip=ip,
            usesoftware=usesoftware,
            location=location,
            dept=dept,
            effect=effect,
            remark=remark,
            status=status,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_JOB_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_JOB插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_JOB插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await IC_JOB(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await IC_JOB(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_RESOURCE_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_RESOURCE插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await IC_RESOURCE(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await IC_RESOURCE(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_RESOURCE_GROUP_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE_GROUP插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_RESOURCE_GROUP插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await IC_RESOURCE_GROUP(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await IC_RESOURCE_GROUP(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await IC_SOURCE_DATABASE(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await IC_SOURCE_DATABASE(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_TABLE_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE_TABLE插入/更新
      required: True
      schema:
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
          ic_source_database_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')
    ic_source_database_id = form.get('ic_source_database_id')

    try:
        if id:  # update
            effectrows = await IC_SOURCE_DATABASE_TABLE(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ic_source_database_id=ic_source_database_id,
            )
        elif not id:  # create
            effectrows = await IC_SOURCE_DATABASE_TABLE(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ic_source_database_id=ic_source_database_id,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_TABLE_COLUMN_InsOrUp(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE_COLUMN插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: IC_SOURCE_DATABASE_TABLE_COLUMN插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await IC_SOURCE_DATABASE_TABLE_COLUMN(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await IC_SOURCE_DATABASE_TABLE_COLUMN(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def METADATA_InsOrUp(request):
    """
    Description end-point
    ---
    description: METADATA插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: METADATA插入/更新
      required: True
      schema:
        type: object
        properties:
          metaid:
            type: string
          mcid:
            type: string
          resourceno:
            type: string
          standardno:
            type: string
          columnname:
            type: string
          oldcolumnname:
            type: string
          metaname:
            type: string
          metapy:
            type: string
          columntype:
            type: string
          columnlen:
            type: string
          metadefine:
            type: string
          remark:
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
    id = form.get('metaid')
    mcid = form.get('mcid')
    resourceno = form.get('resourceno')
    standardno = form.get('standardno')
    columnname = form.get('columnname')
    oldcolumnname = form.get('oldcolumnname')
    metaname = form.get('metaname')
    metapy = form.get('metapy')
    columntype = form.get('columntype')
    columnlen = form.get('columnlen')
    metadefine = form.get('metadefine')
    remark = form.get('remark')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await METADATA(metaid=id).upd2(mcid=mcid,
            resourceno=resourceno,
            standardno=standardno,
            columnname=columnname,
            oldcolumnname=oldcolumnname,
            metaname=metaname,
            metapy=metapy,
            columntype=columntype,
            columnlen=columnlen,
            metadefine=metadefine,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await METADATA(metaid=next_id(),
            mcid=mcid,
            resourceno=resourceno,
            standardno=standardno,
            columnname=columnname,
            oldcolumnname=oldcolumnname,
            metaname=metaname,
            metapy=metapy,
            columntype=columntype,
            columnlen=columnlen,
            metadefine=metadefine,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def METADATACLASS_InsOrUp(request):
    """
    Description end-point
    ---
    description: METADATACLASS插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: METADATACLASS插入/更新
      required: True
      schema:
        type: object
        properties:
          mcid:
            type: string
          pid:
            type: string
          metaclsno:
            type: string
          classno:
            type: string
          isresource:
            type: string
          level:
            type: string
          metaclsname:
            type: string
          metaclspy:
            type: string
          app:
            type: string
          remark:
            type: string
          createname:
            type: string
          createtime:
            type: string
          updatetime:
            type: string
          
    """
    form = await request.json()
    id = form.get('mcid')
    pid = form.get('pid')
    metaclsno = form.get('metaclsno')
    classno = form.get('classno')
    isresource = form.get('isresource')
    level = form.get('level')
    metaclsname = form.get('metaclsname')
    metaclspy = form.get('metaclspy')
    app = form.get('app')
    remark = form.get('remark')
    createname = form.get('createname')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await METADATACLASS(mcid=id).upd2(pid=pid,
            metaclsno=metaclsno,
            classno=classno,
            isresource=isresource,
            level=level,
            metaclsname=metaclsname,
            metaclspy=metaclspy,
            app=app,
            remark=remark,
            createname=createname,
            createtime=createtime,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await METADATACLASS(mcid=next_id(),
            pid=pid,
            metaclsno=metaclsno,
            classno=classno,
            isresource=isresource,
            level=level,
            metaclsname=metaclsname,
            metaclspy=metaclspy,
            app=app,
            remark=remark,
            createname=createname,
            createtime=createtime,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def NOSQLBASE_InsOrUp(request):
    """
    Description end-point
    ---
    description: NOSQLBASE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: NOSQLBASE插入/更新
      required: True
      schema:
        type: object
        properties:
          ndid:
            type: string
          dbname:
            type: string
          type:
            type: string
          ip:
            type: string
          port:
            type: string
          accountnumber:
            type: string
          password:
            type: string
          remark:
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
    id = form.get('ndid')
    dbname = form.get('dbname')
    type = form.get('type')
    ip = form.get('ip')
    port = form.get('port')
    accountnumber = form.get('accountnumber')
    password = form.get('password')
    remark = form.get('remark')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await NOSQLBASE(ndid=id).upd2(dbname=dbname,
            type=type,
            ip=ip,
            port=port,
            accountnumber=accountnumber,
            password=password,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await NOSQLBASE(ndid=next_id(),
            dbname=dbname,
            type=type,
            ip=ip,
            port=port,
            accountnumber=accountnumber,
            password=password,
            remark=remark,
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def RESOURCEBASE_InsOrUp(request):
    """
    Description end-point
    ---
    description: RESOURCEBASE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: RESOURCEBASE插入/更新
      required: True
      schema:
        type: object
        properties:
          rbid:
            type: string
          name:
            type: string
          datasourceunit:
            type: string
          createunit:
            type: string
          contact:
            type: string
          tel:
            type: string
          status:
            type: string
          createtime:
            type: string
          updatetime:
            type: string
          
    """
    form = await request.json()
    id = form.get('rbid')
    name = form.get('name')
    datasourceunit = form.get('datasourceunit')
    createunit = form.get('createunit')
    contact = form.get('contact')
    tel = form.get('tel')
    status = form.get('status')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await RESOURCEBASE(rbid=id).upd2(name=name,
            datasourceunit=datasourceunit,
            createunit=createunit,
            contact=contact,
            tel=tel,
            status=status,
            createtime=createtime,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await RESOURCEBASE(rbid=next_id(),
            name=name,
            datasourceunit=datasourceunit,
            createunit=createunit,
            contact=contact,
            tel=tel,
            status=status,
            createtime=createtime,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_APPLICATION_RECORD_InsOrUp(request):
    """
    Description end-point
    ---
    description: SC_APPLICATION_RECORD插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_APPLICATION_RECORD插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await SC_APPLICATION_RECORD(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await SC_APPLICATION_RECORD(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_GROUP_InsOrUp(request):
    """
    Description end-point
    ---
    description: SC_GROUP插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_GROUP插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await SC_GROUP(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await SC_GROUP(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_LOG_InsOrUp(request):
    """
    Description end-point
    ---
    description: SC_LOG插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_LOG插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await SC_LOG(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await SC_LOG(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_SERVICE_InsOrUp(request):
    """
    Description end-point
    ---
    description: SC_SERVICE插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_SERVICE插入/更新
      required: True
      schema:
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
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')

    try:
        if id:  # update
            effectrows = await SC_SERVICE(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            )
        elif not id:  # create
            effectrows = await SC_SERVICE(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_SERVICE_REQUEST_PARAMETERS_InsOrUp(request):
    """
    Description end-point
    ---
    description: SC_SERVICE_REQUEST_PARAMETERS插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: SC_SERVICE_REQUEST_PARAMETERS插入/更新
      required: True
      schema:
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
          location:
            type: string
          type:
            type: string
          example:
            type: string
          default:
            type: string
          required:
            type: string
          rmark:
            type: string
          sc_service_id:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    createuserid = form.get('createuserid')
    createtime = form.get('createtime')
    updateuserid = form.get('updateuserid')
    updatetime = form.get('updatetime')
    name = form.get('name')
    location = form.get('location')
    type = form.get('type')
    example = form.get('example')
    default = form.get('default')
    required = form.get('required')
    rmark = form.get('rmark')
    sc_service_id = form.get('sc_service_id')

    try:
        if id:  # update
            effectrows = await SC_SERVICE_REQUEST_PARAMETERS(id=id).upd2(createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            name=name,
            location=location,
            type=type,
            example=example,
            default=default,
            required=required,
            rmark=rmark,
            sc_service_id=sc_service_id,
            )
        elif not id:  # create
            effectrows = await SC_SERVICE_REQUEST_PARAMETERS(id=next_id(),
            createuserid=createuserid,
            createtime=createtime,
            updateuserid=updateuserid,
            updatetime=updatetime,
            name=name,
            location=location,
            type=type,
            example=example,
            default=default,
            required=required,
            rmark=rmark,
            sc_service_id=sc_service_id,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def USERS_InsOrUp(request):
    """
    Description end-point
    ---
    description: USERS插入/更新 没有id表示插入 有id表示更新
    tags:
    - insert update
    produces:
    - application/json
    parameters:
    - in: body
      name: body
      description: USERS插入/更新
      required: True
      schema:
        type: object
        properties:
          id:
            type: string
          email:
            type: string
          passwd:
            type: string
          admin:
            type: string
          name:
            type: string
          image:
            type: string
          created_at:
            type: string
          
    """
    form = await request.json()
    id = form.get('id')
    email = form.get('email')
    passwd = form.get('passwd')
    admin = form.get('admin')
    name = form.get('name')
    image = form.get('image')
    created_at = form.get('created_at')

    try:
        if id:  # update
            effectrows = await USERS(id=id).upd2(email=email,
            passwd=passwd,
            admin=admin,
            name=name,
            image=image,
            created_at=created_at,
            )
        elif not id:  # create
            effectrows = await USERS(id=next_id(),
            email=email,
            passwd=passwd,
            admin=admin,
            name=name,
            image=image,
            created_at=created_at,
            ).save()
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

