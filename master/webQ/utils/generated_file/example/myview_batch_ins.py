import json, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, render_json, render_image
from webQ.q_helpers import next_id, Page, ToMysqlDateTimeNow
from model import *


async def BLOODEDGE_BatchIns(request):
    """
    Description end-point
    ---
    description: BLOODEDGE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await BLOODEDGE(beid=next_id(),
            srcid=n.get('srcid'),
            dstid=n.get('dstid'),
            relation=n.get('relation'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def DATALAYER_BatchIns(request):
    """
    Description end-point
    ---
    description: DATALAYER批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await DATALAYER(dlid=next_id(),
            name=n.get('name'),
            shortname=n.get('shortname'),
            effect=n.get('effect'),
            remark=n.get('remark'),
            status=n.get('status'),
            sort=n.get('sort'),
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


async def DBTABLE_BatchIns(request):
    """
    Description end-point
    ---
    description: DBTABLE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await DBTABLE(tabid=next_id(),
            rbid=n.get('rbid'),
            dlid=n.get('dlid'),
            tablenameyw=n.get('tablenameyw'),
            tablenamezw=n.get('tablenamezw'),
            remark=n.get('remark'),
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


async def DBTABLE_RELATION_BatchIns(request):
    """
    Description end-point
    ---
    description: DBTABLE_RELATION批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await DBTABLE_RELATION(id=next_id(),
            primary_table_id=n.get('primary_table_id'),
            slave_talbe_id=n.get('slave_talbe_id'),
            type=n.get('type'),
            name=n.get('name'),
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


async def DBTABLECOLUMN_BatchIns(request):
    """
    Description end-point
    ---
    description: DBTABLECOLUMN批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await DBTABLECOLUMN(colid=next_id(),
            tabid=n.get('tabid'),
            metaid=n.get('metaid'),
            ispk=n.get('ispk'),
            isnull=n.get('isnull'),
            isuq=n.get('isuq'),
            range=n.get('range'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def FRONTBASE_BatchIns(request):
    """
    Description end-point
    ---
    description: FRONTBASE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await FRONTBASE(fbid=next_id(),
            name=n.get('name'),
            ip=n.get('ip'),
            usesoftware=n.get('usesoftware'),
            location=n.get('location'),
            dept=n.get('dept'),
            effect=n.get('effect'),
            remark=n.get('remark'),
            status=n.get('status'),
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


async def IC_JOB_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_JOB批量插入
    tags:
    - insert batch
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
            effectrows = await IC_JOB(id=next_id(),
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


async def IC_RESOURCE_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE批量插入
    tags:
    - insert batch
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
            effectrows = await IC_RESOURCE(id=next_id(),
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


async def IC_RESOURCE_GROUP_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_RESOURCE_GROUP批量插入
    tags:
    - insert batch
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
            effectrows = await IC_RESOURCE_GROUP(id=next_id(),
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


async def IC_SOURCE_DATABASE_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE批量插入
    tags:
    - insert batch
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
            effectrows = await IC_SOURCE_DATABASE(id=next_id(),
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


async def IC_SOURCE_DATABASE_TABLE_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE批量插入
    tags:
    - insert batch
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
                ic_source_database_id:
                  type: string
                
    """
    form = await request.json()
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await IC_SOURCE_DATABASE_TABLE(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            ic_source_database_id=n.get('ic_source_database_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def IC_SOURCE_DATABASE_TABLE_COLUMN_BatchIns(request):
    """
    Description end-point
    ---
    description: IC_SOURCE_DATABASE_TABLE_COLUMN批量插入
    tags:
    - insert batch
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
            effectrows = await IC_SOURCE_DATABASE_TABLE_COLUMN(id=next_id(),
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


async def METADATA_BatchIns(request):
    """
    Description end-point
    ---
    description: METADATA批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await METADATA(metaid=next_id(),
            mcid=n.get('mcid'),
            resourceno=n.get('resourceno'),
            standardno=n.get('standardno'),
            columnname=n.get('columnname'),
            oldcolumnname=n.get('oldcolumnname'),
            metaname=n.get('metaname'),
            metapy=n.get('metapy'),
            columntype=n.get('columntype'),
            columnlen=n.get('columnlen'),
            metadefine=n.get('metadefine'),
            remark=n.get('remark'),
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


async def METADATACLASS_BatchIns(request):
    """
    Description end-point
    ---
    description: METADATACLASS批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await METADATACLASS(mcid=next_id(),
            pid=n.get('pid'),
            metaclsno=n.get('metaclsno'),
            classno=n.get('classno'),
            isresource=n.get('isresource'),
            level=n.get('level'),
            metaclsname=n.get('metaclsname'),
            metaclspy=n.get('metaclspy'),
            app=n.get('app'),
            remark=n.get('remark'),
            createname=n.get('createname'),
            createtime=n.get('createtime'),
            updatetime=n.get('updatetime'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def NOSQLBASE_BatchIns(request):
    """
    Description end-point
    ---
    description: NOSQLBASE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await NOSQLBASE(ndid=next_id(),
            dbname=n.get('dbname'),
            type=n.get('type'),
            ip=n.get('ip'),
            port=n.get('port'),
            accountnumber=n.get('accountnumber'),
            password=n.get('password'),
            remark=n.get('remark'),
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


async def RESOURCEBASE_BatchIns(request):
    """
    Description end-point
    ---
    description: RESOURCEBASE批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await RESOURCEBASE(rbid=next_id(),
            name=n.get('name'),
            datasourceunit=n.get('datasourceunit'),
            createunit=n.get('createunit'),
            contact=n.get('contact'),
            tel=n.get('tel'),
            status=n.get('status'),
            createtime=n.get('createtime'),
            updatetime=n.get('updatetime'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def SC_APPLICATION_RECORD_BatchIns(request):
    """
    Description end-point
    ---
    description: SC_APPLICATION_RECORD批量插入
    tags:
    - insert batch
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
            effectrows = await SC_APPLICATION_RECORD(id=next_id(),
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


async def SC_GROUP_BatchIns(request):
    """
    Description end-point
    ---
    description: SC_GROUP批量插入
    tags:
    - insert batch
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
            effectrows = await SC_GROUP(id=next_id(),
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


async def SC_LOG_BatchIns(request):
    """
    Description end-point
    ---
    description: SC_LOG批量插入
    tags:
    - insert batch
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
            effectrows = await SC_LOG(id=next_id(),
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


async def SC_SERVICE_BatchIns(request):
    """
    Description end-point
    ---
    description: SC_SERVICE批量插入
    tags:
    - insert batch
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
            effectrows = await SC_SERVICE(id=next_id(),
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


async def SC_SERVICE_REQUEST_PARAMETERS_BatchIns(request):
    """
    Description end-point
    ---
    description: SC_SERVICE_REQUEST_PARAMETERS批量插入
    tags:
    - insert batch
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await SC_SERVICE_REQUEST_PARAMETERS(id=next_id(),
            createuserid=n.get('createuserid'),
            createtime=n.get('createtime'),
            updateuserid=n.get('updateuserid'),
            updatetime=n.get('updatetime'),
            name=n.get('name'),
            location=n.get('location'),
            type=n.get('type'),
            example=n.get('example'),
            default=n.get('default'),
            required=n.get('required'),
            rmark=n.get('rmark'),
            sc_service_id=n.get('sc_service_id'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def USERS_BatchIns(request):
    """
    Description end-point
    ---
    description: USERS批量插入
    tags:
    - insert batch
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
          batch_data:
            type: array
            items:
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
    data_list = form.get('batch_data')

    try:
        for n in data_list:
            effectrows = await USERS(id=next_id(),
            email=n.get('email'),
            passwd=n.get('passwd'),
            admin=n.get('admin'),
            name=n.get('name'),
            image=n.get('image'),
            created_at=n.get('created_at'),
            ).save()

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)

