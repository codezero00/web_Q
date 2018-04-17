import json, time, hashlib, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json
from webQ.q_login import _COOKIE_NAME, encode_cookie
from webQ.q_helpers import _RE_EMAIL, _RE_SHA1, APIValueError, APIError, next_id, Page, ToMysqlDateTimeNow
# from model import User, VFrontBase, VDataLayer, MetaDataClass, VMetadataClass, VMetaData, VResourceBase, VDBTableTree, \
#     VDBTableLayerTree, VDBTable, VDBTableColumn, VETLClients, VEtlJobs
from model import *
from utils import parestree
from etlcarte import ETLCarte
from cls_dnn import forecast
import pandas as pd


# def render_json(data):
#     r = Response()
#     r.content_type = 'application/json'
#     r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
#     return r

# region ai

async def ai(request):
    content = request.query.get('content')
    content2 = forecast(content)
    print(content2)

    data = dict()
    data['success'] = True
    data['data'] = content2
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


# endregion


# region login

async def authenticate(request):
    '''
    登陆模块
    :param request:
    :return:
    '''
    # data = await request.json()
    # email = data['email']
    # passwd = data['passwd']
    email = request.query.get('email')
    passwd = request.query.get('passwd')
    if not email:
        raise Exception('email', 'Invalid email.')
    if not passwd:
        raise Exception('passwd', 'Invalid password.')
    users = await User.findAll('email=?', [email])
    if len(users) == 0:
        raise Exception('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    print(sha1.hexdigest())
    print('passwd: {}'.format(user.passwd))

    # if user.passwd != sha1.hexdigest():
    #     raise Exception('passwd', 'Invalid password.')

    # authenticate ok, set cookie:
    r = Response()
    r.content_type = 'application/json'
    data = dict()

    if user.passwd == sha1.hexdigest():
        r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400)
        user.passwd = '******'
        data['success'] = True
        data['data'] = user
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return r
    else:
        data['failure'] = 'Invalid password.'
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return r


async def api_register_user(request):
    # def api_register_user(*, email, name, passwd):
    '''
    用户注册模块
    :param email:
    :param name:
    :param passwd:
    :return:
    '''
    email = request.query.get('email')
    name = request.query.get('name')
    passwd = request.query.get('passwd')
    print('e: {} n: {} p: {}'.format(email, name, passwd))
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    # if not passwd or not _RE_SHA1.match(passwd):
    if not passwd:
        raise APIValueError('passwd')
    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(),
                image='http://xxx/qq?d=mm&s=120')
    await user.save()
    # make session cookie:
    r = Response()
    # r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400, httponly=True)
    r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


# async def islogin(request):
#     if request.__user__:
#         ##
#         data = dict()
#         data['success'] = True
#         # data4['failure'] = None
#         data['data'] = request.__user__
#         ##
#         r = Response()
#         # request.__user__.passwd = '******'
#         r.content_type = 'application/json'
#         r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
#         # r.body = json.dumps(request.__user__, ensure_ascii=False).encode('utf-8')
#         return r
#     else:
#         raise APIError('do not login! plase login!')

async def islogin(request):
    # if request.__user__:
    if True:  # 暂时修改 登陆权限取消
        ##
        data = dict()
        data['success'] = True
        # data4['failure'] = None
        users = await User.findAll('email=?', ["258607438@qq.com"])
        data['data'] = users[0]
        ##
        r = Response()
        # request.__user__.passwd = '******'
        r.content_type = 'application/json'
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        # r.body = json.dumps(request.__user__, ensure_ascii=False).encode('utf-8')
        return r
    else:
        raise APIError('do not login! plase login!')


# endregion


# region test
def index(request):
    return Response(body=u'<h1>hello word</h1>')


def index1(request):
    data = {
        '__template__': 'index.html',
        'data': '...'
    }
    # if isinstance(data,dict):
    #     rep=web.Response(body=app[__])
    return Response(body=u'<h1>hello word1111111111</h1>')


def index2(request):
    url_param = request.match_info['gid']
    print(request)
    print(url_param)
    return Response(body=u'<h1>hello word！ {},{}</h1>'.format(request, url_param))


def index3(request):
    data = {
        'id': '1',
        'name': 'akeec',
        'desc': '啊哈哈哈'
    }
    return json_response(data)


def index4(request):
    data = {
        'id': '2222',
        'name': 'akeec',
        'desc': 'okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
    }
    rep = Response()
    rep.set_cookie('P_UID', 'AGASGLKSAEG', max_age=86400, httponly=True)
    rep.content_type = 'application/json'
    rep.body = (json.dumps(data, ensure_ascii=False).encode('utf-8'))
    return rep


async def index5(request):
    mysql = "SELECT 42;"
    print(mysql)
    list = await orm.select(p_sql=mysql, param={})
    print('endddddddddddddd{}'.format(str(list)))
    return str(list)


def index6(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    # ]
    blogs = [
        ('1', 'Test Blog', summary, time.time() - 120),
        ('2', 'Something New', summary, time.time() - 3600),
        ('3', 'Learn Swift', summary, time.time() - 7200)
    ]
    return {
        '__template__': 'weekgaplist.html',
        'data': blogs
    }


async def index7(request):
    '''
    通过连接池完成mysql查询
    :param request:
    :return:
    '''
    logging.info('get int index7777')
    list = await orm.test_example()
    print('endddddddddddddd{}'.format(str(list)))
    return str(list)


async def index8(request):
    '''
    :param request:
    :return:
    '''
    logging.info('get int index8')
    list = await model.weekgaplist()
    res = [{'code': i[0], 'name': i[1], 'industry': i[2], 'today': i[3], 'yesterday': i[4], 'tod_high': i[5],
            'tod_low': i[6], 'yes_high': i[7], 'yes_low': i[8], 'gaptype': i[9], 'gapdesc': i[10]} for i in list]
    return json_response(res)


async def index90(request):
    '''
    :param request: sharecode
    :return:
    '''
    logging.info('get int index90')
    __sharecode = await request.json()
    list = await model.getonegap(sharecode=str(__sharecode["sharecode"]))
    res = [{'code': i[0], 'name': i[1], 'industry': i[2], 'today': i[3], 'yesterday': i[4], 'tod_high': i[5],
            'tod_low': i[6], 'yes_high': i[7], 'yes_low': i[8], 'gaptype': i[9], 'gapdesc': i[10]} for i in list]
    return json_response(res)


async def index9(request):
    '''
    :param request:
    :return:
    '''
    logging.info('get int index9')
    list = await model.weekgaplist()
    data = [{'code': i[0], 'name': i[1], 'industry': i[2], 'today': i[3], 'yesterday': i[4], 'tod_high': i[5],
             'tod_low': i[6], 'yes_high': i[7], 'yes_low': i[8], 'gaptype': i[9], 'gapdesc': i[10]} for i in list]
    data2 = {'success': True}
    data3 = {'failure': '错了哈哈哈'}
    data4 = dict()
    data4['success'] = True
    data4['failure'] = None
    data4['data'] = data
    print(data4)
    # rep = web.Response(headers={'Access-Control-Allow-Origin':'*'}) ##headers中Access-Control-Allow-Origin':'*'表示跨域权限
    rep = Response()
    rep.content_type = 'application/json;charset=utf-8'  ##charset=utf-8 不加会出现乱码，application/json 不加会出现下周框
    rep.body = json.dumps(data3, ensure_ascii=False).encode('utf8')
    return rep


async def index10(request):
    '''
    :param request:
    :return:
    '''
    logging.info('get int index10')
    list = await model.weekgaplist()
    data = [{'code': i[0], 'name': i[1], 'industry': i[2], 'today': i[3], 'yesterday': i[4], 'tod_high': i[5],
             'tod_low': i[6], 'yes_high': i[7], 'yes_low': i[8], 'gaptype': i[9], 'gapdesc': i[10]} for i in list]
    data2 = {'success': True}
    data3 = {'failure': '错了哈哈哈'}
    data4 = {
        'success': True,
        'failure': 'ora-021461 balabala!!!',
        'data': data
    }
    rep = Response(headers={'Access-Control-Allow-Origin': '*'})  ##headers中Access-Control-Allow-Origin':'*'表示跨域权限
    # rep = web.Response()
    rep.content_type = 'application/json;charset=utf-8'
    rep.body = json.dumps(data4, ensure_ascii=False).encode('utf8')
    return rep


async def index11(request):
    '''
    :param request:
    :return:
    '''
    logging.info('get int index11')
    # data2 = await  request.json()
    # print(data2[0])
    # __sharecode = request.query.get('sharecode') ##form get 获取get数据
    # sharecode = __sharecode
    __sharecode = await request.json()
    list = await model.getonegap(sharecode=str(__sharecode["sharecode"]))
    data = [{'code': i[0], 'name': i[1], 'industry': i[2], 'today': i[3], 'yesterday': i[4], 'tod_high': i[5],
             'tod_low': i[6], 'yes_high': i[7], 'yes_low': i[8], 'gaptype': i[9], 'gapdesc': i[10]} for i in list]
    data4 = dict()
    data4['success'] = True
    data4['failure'] = None
    data4['data'] = data
    print(data4)
    # rep = web.Response(headers={
    #     "Access-Control-Allow-Origin":"*",
    #     "Access-Control-Allow-Headers":"X-Requested-With, accept, origin, content-type",
    #     "Access-Control-Allow-Methods":"PUT,POST,GET,DELETE,OPTIONS",
    #                             }) ##headers中Access-Control-Allow-Origin':'*'表示跨域权限
    rep = Response()
    rep.content_type = 'application/json;charset=utf-8'  ##charset=utf-8 不加会出现乱码，application/json 不加会出现下周框
    rep.body = json.dumps(data4, ensure_ascii=False).encode('utf8')
    return rep


async def index12(request):
    data = await User.find(1)
    print(data)
    return json_response(data)


# endregion


# region metadata
async def metaclasstreeQuery(request):
    # if request.__user__:
    group = await MetaDataClass.findAll()
    group_list = [
        {'ID': str(i['metaclsid']), 'PID': str(i['parentid']), 'NAME': i['metaclsname'], 'ISRESOURCE': i['isresource']}
        for i in group]
    # print(group_list)
    ##
    data = dict()
    data['success'] = True
    # data4['failure'] = None
    data['data'] = parestree(group_list)
    ##
    r = Response()
    # request.__user__.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    # r.body = json.dumps(request.__user__, ensure_ascii=False).encode('utf-8')
    return r
    # else:
    #     raise APIError('do not login! plase login!')


async def metaclassQuery(request):
    id = request.query.get('id')
    upclass = await VMetadataClass.findAll(where=f'FLBM = "{id}"')
    upclass_list = {'upclass': upclass}
    downclass = await VMetadataClass.findAll(where=f'PID = "{id}"')
    downclass_list = {'downclass': downclass}
    # print(downclass)

    data = dict()
    data['success'] = True
    data['data'] = dict(**upclass_list, **downclass_list)  # 合并dict
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r
    # else:
    #     raise APIError('do not login! plase login!')


async def metadatadetailQuery(request):
    id = request.query.get('id')
    metadata = await VMetaData.findAll(where=f'PID = "{id}"')
    ##
    data = dict()
    data['success'] = True
    data['data'] = metadata
    ##
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r
    # else:
    #     raise APIError('do not login! plase login!')


async def FrontBaseQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await VFrontBase.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await VFrontBase.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)
    # dblist = await VFrontBase.findAll()
    # data = dict()
    # data['success'] = True
    # data['data'] = dblist
    # r = Response()
    # r.content_type = 'application/json'
    # r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    # return r


async def ResourceBaseQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await VResourceBase.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await VResourceBase.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)
    # dblist = await VResourceBase.findAll()
    # data = dict()
    # data['success'] = True
    # data['data'] = dblist
    # r = Response()
    # r.content_type = 'application/json'
    # r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    # return r


async def DataLayerQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await VDataLayer.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await VDataLayer.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def dbtabletreeQuery(request):
    tabletreelist = await VDBTableTree.findAll()
    data = dict()
    data['success'] = True
    data['data'] = parestree(tabletreelist)
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def DBTableLayerTreeQuery(request):
    tabletreelist = await VDBTableLayerTree.findAll()
    data = dict()
    data['success'] = True
    data['data'] = parestree(tabletreelist)
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def GetTableQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    else:
        try:
            num = await VDBTable.findNumber(selectField='count(*)')
            p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
            if num == 0:
                data1 = dict(page=p.GetDict, res=[])
            else:
                list = await VDBTable.findAll(limit=(p.offset, p.limit))
                data1 = dict(page=p.GetDict, res=list)
            data = dict(success=True, data=data1)
            return render_json(data)
        except Exception as e:
            data = dict(failure=True, data=e)
            return render_json(data)


async def dbtableQuery(request):
    id = request.query.get('id')
    if not id:
        tablelist = await VDBTable.findAll()
    else:
        tablelist = await VDBTable.findAll(where=f'TABID = "{id}"')
    data = dict()
    data['success'] = True
    data['data'] = tablelist
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def dbtablecolumnQuery(request):
    id = request.query.get('id')
    columnlist = await VDBTableColumn.findAll(where=f'TABID = "{id}"')
    data = dict()
    data['success'] = True
    data['data'] = columnlist
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def etlclientsQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await VETLClients.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await VETLClients.findAll(limit=(p.offset, p.limit))
            for x in list:
                try:
                    client = ETLCarte(x['URL'])  # 实例化carte类
                    y = client.get_status()  # 获取状态
                    x['ZT'] = str(y)  # 将Y赋值给ZT字典
                except:
                    x['ZT'] = 'Offline'
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)
    # clientslist = await VETLClients.findAll()
    # for x in clientslist:
    #     try:
    #         client = ETLCarte(x['URL'])  # 实例化carte类
    #         y = client.get_status()  # 获取状态
    #         x['ZT'] = str(y)  # 将Y赋值给ZT字典
    #     except:
    #         x['ZT'] = 'Offline'
    # data = dict()
    # data['success'] = True
    # data['data'] = clientslist
    # r = Response()
    # r.content_type = 'application/json'
    # r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    # return r


async def EtlJobsQuery(request):
    clientslist = await VETLClients.findAll()
    jobslist = await VEtlJobs.findAll()
    jbl = []
    for x in clientslist:
        try:
            client = ETLCarte(x['URL'])  # 实例化carte类
            jobs = client.get_jobs()  # 获取状态
            jbl += list({'name': x.jobname, 'status': x.status_desc, 'jobnum': x.id} for x in jobs)
        except:
            pass
    jobslist = pd.DataFrame(jobslist)
    jobslist2 = pd.DataFrame(jbl)
    jobslist = pd.merge(jobslist, jobslist2, left_on='name', right_on='name', how='left').fillna('未匹配')  # fillna 填充空值
    # print(jbl)
    mm = jobslist.to_dict(orient='record')  # pandsa df 转 dict
    # print(mm)
    data = dict()
    data['success'] = True
    data['data'] = mm
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


# endregion


# region metadata update del create

# FrontBase
async def FrontBaseInsOrUp(request):
    form = await request.json()
    print(form)
    print(type(form))
    fbid = form.get('fbid')
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
    isdel = form.get('isdel', 1)
    try:
        # num = await FrontBase.findNumber(selectField='count(*)', where=f"fbid='{fbid}'")
        # print(num)
        if fbid and isdel == 1:  # update
            effectrows = await FrontBase(fbid=fbid,
                                         name=name,
                                         ip=ip,
                                         usesoftware=usesoftware,
                                         location=location,
                                         dept=dept,
                                         effect=effect,
                                         remark=remark,
                                         status=status,
                                         # createuserid=createuserid,
                                         # createtime=createtime,
                                         updateuserid=updateuserid,
                                         updatetime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).upd()
        elif not fbid:  # create
            effectrows = await FrontBase(fbid=next_id(),
                                         name=name,
                                         ip=ip,
                                         usesoftware=usesoftware,
                                         location=location,
                                         dept=dept,
                                         effect=effect,
                                         remark=remark,
                                         status=status,
                                         createuserid=createuserid,
                                         createtime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).save()
        elif fbid and isdel == 0:  # delete
            effectrows = await FrontBase(fbid=fbid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def FrontBaseDelete(request):
    """
    物理删除~暂时不使用
    :param request:
    :return:
    """
    rbid = request.query.get('rbid')
    if (not rbid):
        data = dict(failure=True, data="find no id!")
        return render_json(data)
    try:
        effectrows = await FrontBase(fbid=rbid).rm()
        if effectrows >= 1:
            data = dict(success=True, data=effectrows)
        else:
            data = dict(failure=True, data='delete fuilure!')
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=str(e))
        return render_json(data)


# ResourceBase
async def ResourceBaseInsOrUp(request):
    form = await request.json()
    rbid = form.get('rbid')
    name = form.get('name')
    datasourceunit = form.get('datasourceunit')
    createunit = form.get('createunit')
    contact = form.get('contact')
    tel = form.get('tel')
    status = form.get('status')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')
    isdel = form.get('isdel', 1)
    try:

        if rbid and isdel == 1:  # update
            effectrows = await ResourceBase(rbid=rbid,
                                         name=name,
                                         datasourceunit=datasourceunit,
                                         createunit=createunit,
                                         contact=contact,
                                         tel=tel,
                                         status=status,
                                         updatetime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).upd()
        elif not rbid:  # create
            effectrows = await ResourceBase(rbid=next_id(),
                                         name=name,
                                         datasourceunit=datasourceunit,
                                         createunit=createunit,
                                         contact=contact,
                                         tel=tel,
                                         status=status,
                                         createtime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).save()
        elif rbid and isdel == 0:  # delete
            effectrows = await ResourceBase(rbid=rbid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# DataLayer
async def DataLayerInsOrUp(request):
    form = await request.json()
    dlid = form.get('dlid')
    name = form.get('name')
    shortname = form.get('shortname')
    effect = form.get('effect')
    remark = form.get('remark')
    status = form.get('status')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')
    isdel = form.get('isdel', 1)
    try:

        if dlid and isdel == 1:  # update
            effectrows = await DataLayer(dlid=dlid,
                                         name=name,
                                         shortname=shortname,
                                         effect=effect,
                                         remark=remark,
                                         status=status,
                                         updateuserid=updateuserid,
                                         updatetime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).upd()
        elif not dlid:  # create
            effectrows = await DataLayer(dlid=next_id(),
                                         name=name,
                                         shortname=shortname,
                                         effect=effect,
                                         remark=remark,
                                         status=status,
                                         createuserid=createuserid,
                                         createtime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).save()
        elif dlid and isdel == 0:  # delete
            effectrows = await DataLayer(dlid=dlid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# DBTable
async def DBTableInsOrUp(request):
    form = await request.json()
    tabid = form.get('tabid')
    rbid = form.get('rbid')
    dlid = form.get('dlid')
    tablenameyw = form.get('tablenameyw')
    tablenamezw = form.get('tablenamezw')
    remark = form.get('remark')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')
    isdel = form.get('isdel', 1)
    try:

        if tabid and isdel == 1:  # update
            effectrows = await DBTable(tabid=tabid,
                                         rbid=rbid,
                                         dlid=dlid,
                                         tablenameyw=tablenameyw,
                                         tablenamezw=tablenamezw,
                                         remark=remark,
                                         updateuserid=updateuserid,
                                         updatetime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).upd()
        elif not tabid:  # create
            effectrows = await DBTable(tabid=next_id(),
                                         rbid=rbid,
                                         dlid=dlid,
                                         tablenameyw=tablenameyw,
                                         tablenamezw=tablenamezw,
                                         remark=remark,
                                         createuserid=createuserid,
                                         createtime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).save()
        elif tabid and isdel == 0:  # delete
            effectrows = await DBTable(tabid=tabid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# ETLClients
async def ETLClientsInsOrUp(request):
    form = await request.json()
    etlid = form.get('etlid')
    name = form.get('name')
    ip = form.get('ip')
    port = form.get('port')
    url = form.get('url')
    version = form.get('version')
    location = form.get('location')
    desc = form.get('desc')
    createuserid = form.get('createuserid')
    updateuserid = form.get('updateuserid')
    createtime = form.get('createtime')
    updatetime = form.get('updatetime')
    isdel = form.get('isdel', 1)
    try:

        if etlid and isdel == 1:  # update
            effectrows = await ETLClients(etlid=etlid,
                                         name=name,
                                         ip=ip,
                                         port=port,
                                         url=url,
                                         version=version,
                                         location=location,
                                         desc=desc,
                                         updateuserid=updateuserid,
                                         updatetime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).upd()
        elif not etlid:  # create
            effectrows = await ETLClients(etlid=next_id(),
                                         name=name,
                                         ip=ip,
                                         port=port,
                                         url=url,
                                         version=version,
                                         location=location,
                                         desc=desc,
                                         createuserid=createuserid,
                                         createtime=ToMysqlDateTimeNow(),
                                         isdel=isdel
                                         ).save()
        elif etlid and isdel == 0:  # delete
            effectrows = await ETLClients(etlid=etlid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# endregion


# region websokect

async def websocket_handler(request):
    ws = WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


import time
import random


async def websocket_handler_test1(request):
    ws = WebSocketResponse()
    print(ws)
    await ws.prepare(request)
    x = 0
    y = 0
    async for msg in ws:
        print(msg.data)
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                while True:
                    y = x
                    x += random.randint(10, 20)
                    await ws.send_str(str(x) + ',' + str(y))
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())
            ws.close()

    print('websocket connection closed')

    return ws


async def websocket_handler_test3(request):
    ws = WebSocketResponse()
    await ws.prepare(request)
    test3 = []
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                test3.append()
                await ws.send_str(msg.data + '/answer')
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


async def wshandler(request):
    resp = WebSocketResponse()
    # ok, protocol = resp.can_prepare(request)
    # if not ok:
    #     with open(WS_FILE, 'rb') as fp:
    #         return Response(body=fp.read(), content_type='text/html')

    await resp.prepare(request)

    print(request.app['sockets'])
    try:
        print('Someone joined.')
        for ws in request.app['sockets']:
            await ws.send_str('Someone joined')
        request.app['sockets'].append(resp)

        async for msg in resp:
            if msg.type == WSMsgType.TEXT:
                for ws in request.app['sockets']:
                    if ws is not resp:
                        await ws.send_str(msg.data)
            else:
                return resp
        return resp

    finally:
        request.app['sockets'].remove(resp)
        print('Someone disconnected.')
        for ws in request.app['sockets']:
            await ws.send_str('Someone disconnected.')


async def on_shutdown(app):
    for ws in app['sockets']:
        await ws.close()

# endregion
