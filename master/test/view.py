import json, time, hashlib, logging, model
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response, WebSocketResponse, WSMsgType, render_json, render_image
from webQ.q_login import _COOKIE_NAME, encode_cookie
from webQ.q_helpers import _RE_EMAIL, _RE_SHA1, APIValueError, APIError, next_id, Page, ToMysqlDateTimeNow
from model import *
from utils import parestree, parescolumntree
from etlcarte import ETLCarte
from cls_dnn import forecast
from cls_word2vec import GenKeywords
import pandas as pd
# from gfs import GFS
from aiogfs import GFS
from bson.objectid import ObjectId
from cls_face_net import compare_two_bytes
import re


# def render_json(data):
#     r = Response()
#     r.content_type = 'application/json'
#     r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
#     return r

# def render_image(data):
#     r = Response()
#     r.content_type = 'image/jpeg'
#     r.body = data
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


async def Word2vecKeywords(request):
    content = request.query.get('content')
    content2 = GenKeywords(content)
    print(content2)

    data = dict()
    data['success'] = True
    data['data'] = content2
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


imgdict = {'sourceimg': None,
           'targetimg': None
           }


async def SourceUpload(request):
    form = await request.post()
    form = dict(**form)
    file = form.get('file')
    file = file.file
    image = file.read()
    # print(image)
    imgdict['sourceimg'] = image
    if image:
        effectrows = 1
        data = dict(success=True, data=effectrows)
        return render_json(data)
    else:
        data = dict(failure=True, data='no data!')
        return render_json(data)


async def TargetUpload(request):
    form = await request.post()
    form = dict(**form)
    file = form.get('file')
    file = file.file
    image = file.read()
    # print(image)
    imgdict['targetimg'] = image
    if image:
        effectrows = 1
        data = dict(success=True, data=effectrows)
        return render_json(data)
    else:
        data = dict(failure=True, data='no data!')
        return render_json(data)


async def AIFaceCompare(request):
    """
    use: action=http://127.0.0.1:9000/api/v1/AIUploadFile1
    :param request:
    :return:
    """
    res = ''
    print(imgdict)
    if imgdict['targetimg'] and imgdict['sourceimg']:
        forecastvalue = compare_two_bytes(sourceimgbytes=imgdict['sourceimg'],
                                          targetimgbytes=imgdict['targetimg'])
        print(f'forecast value: {forecastvalue}')
        if forecastvalue > 0.9:
            res = f'不是同一个人({forecastvalue})'
        elif forecastvalue >= 0.8 and forecastvalue <= 0.9:
            res = f'很像({forecastvalue})'
        elif forecastvalue < 0.8:
            res = f'是同一个人({forecastvalue})'
        else:
            res = '不是同一个人'
    try:
        effectrows = res
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


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
    group = await MetaDataClass.findAll(where=f'isdel = 1')
    group_list = [
        {'ID': str(i['mcid']), 'PID': str(i['pid']), 'NAME': i['metaclsname'], 'ISRESOURCE': i['isresource'],
         'METACLSNO': i['metaclsno']}
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
    upclass = await VMetadataClass.findAll(where=f'MCID = "{id}"')
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
    _col = request.query.get('col', 1)
    _str = request.query.get('str', 1)
    if str(_col).strip() == '' or str(_str).strip() == '':
        _col, _str = 1, 1
    metadata = await VMetaData.findAll(where=f'PID = "{id}" and {_col} REGEXP "{_str}"')
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


async def dbtablecolumn2Query(request):
    id = request.query.get('id')
    columnlist = await VDBTableColumn2.findAll(where=f'TABID = "{id}"')
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


from io import StringIO, BytesIO


async def EtlJobImage(request):
    Url = request.query.get('Url')
    Jobid = request.query.get('Jobid')
    img = None
    # try:
    client = ETLCarte(Url)  # 实例化carte类
    x = client.get_image(id=Jobid)  # 获取图片 类型 PIL.PNG
    # z = client.get_job_status(id=Jobid, name='test2')
    # print(z)
    buf = BytesIO()
    x.save(buf, format='png')  # 转2进制bytes类型
    y = buf.getvalue()
    # print(y)
    # print(type(y))
    img = y
    # except Exception as e:
    #     print(e)
    # r = Response()
    # r.content_type = 'image/jpeg'
    # r.body = img
    return render_image(img)


import aiohttp
from bs4 import BeautifulSoup


async def EtlJobLog(request):
    Url = request.query.get('Url')
    JobName = request.query.get('JobName')
    print(Url)
    print(JobName)
    auth = aiohttp.BasicAuth(login='cluster', password='cluster', encoding='utf8')
    async with aiohttp.ClientSession(auth=auth) as session:
        async with session.get(Url + "jobStatus/?name=" + JobName) as r:
            json_body = await r.text()
            soup = BeautifulSoup(json_body, "lxml")
            logtext = soup.find(id='joblog')
            data = dict()
            data['success'] = True
            data['data'] = logtext.contents[0]
            return render_json(data)


async def BloodRelationQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    try:
        num = await VBloodRelation.findNumber(selectField='count(*)')
        p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
        if num == 0:
            data1 = dict(page=p.GetDict, res=[])
        else:
            list = await VBloodRelation.findAll(limit=(p.offset, p.limit))
            data1 = dict(page=p.GetDict, res=list)
        data = dict(success=True, data=data1)
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=e)
        return render_json(data)


async def DBTableColumnTreeQuery(request):
    treelist = await VDBTableColumnTree.findAll()
    data = dict()
    data['success'] = True
    data['data'] = parestree(treelist)
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def BloodVertexEdgeQuery(request):
    vertexlist = await VBloodVertex.findAll()
    edgelist = await VBloodEdge.findAll()
    graphlist = dict(vertex=vertexlist, edge=edgelist)
    print(graphlist)
    data = dict()
    data['success'] = True
    data['data'] = graphlist
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def NosqlDatabaseQuery(request):
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    else:
        try:
            num = await VNosqlDatabase.findNumber(selectField='count(*)')
            p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
            if num == 0:
                data1 = dict(page=p.GetDict, res=[])
            else:
                list = await VNosqlDatabase.findAll(limit=(p.offset, p.limit))
                data1 = dict(page=p.GetDict, res=list)
            data = dict(success=True, data=data1)
            return render_json(data)
        except Exception as e:
            data = dict(failure=True, data=e)
            return render_json(data)


async def NosqlBaseTreeQuery(request):
    tabletreelist = await VNosqlBaseTree.findAll()
    print(tabletreelist)
    data = dict()
    data['success'] = True
    data['data'] = parestree(tabletreelist)
    r = Response()
    r.content_type = 'application/json'
    r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return r


async def MetaDataTreeQuery(request):
    treelist = await VMetaDataTree.findAll()
    data = dict()
    data['success'] = True
    data['data'] = parescolumntree(treelist)
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
            effectrows = await FrontBase(fbid=fbid).upd2(name=name,
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
                                                         isdel=isdel)
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
            effectrows = await ResourceBase(rbid=rbid).upd2(name=name,
                                                            datasourceunit=datasourceunit,
                                                            createunit=createunit,
                                                            contact=contact,
                                                            tel=tel,
                                                            status=status,
                                                            updatetime=ToMysqlDateTimeNow(),
                                                            isdel=isdel)
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
            effectrows = await DataLayer(dlid=dlid).upd2(name=name,
                                                         shortname=shortname,
                                                         effect=effect,
                                                         remark=remark,
                                                         status=status,
                                                         updateuserid=updateuserid,
                                                         updatetime=ToMysqlDateTimeNow(),
                                                         isdel=isdel)
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
            effectrows = await DBTable(tabid=tabid).upd2(
                rbid=rbid,
                dlid=dlid,
                tablenameyw=tablenameyw,
                tablenamezw=tablenamezw,
                remark=remark,
                updateuserid=updateuserid,
                updatetime=ToMysqlDateTimeNow(),
                isdel=isdel)

            # effectrows = await DBTable(tabid=tabid,
            #                              rbid=rbid,
            #                              dlid=dlid,
            #                              tablenameyw=tablenameyw,
            #                              tablenamezw=tablenamezw,
            #                              remark=remark,
            #                              updateuserid=updateuserid,
            #                              updatetime=ToMysqlDateTimeNow(),
            #                              isdel=isdel
            #                              ).upd()
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
            effectrows2 = await DBTableColumn(tabid=tabid).upd2(isdel=0)

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
            effectrows = await ETLClients(etlid=etlid).upd2(name=name,
                                                            ip=ip,
                                                            port=port,
                                                            url=url,
                                                            version=version,
                                                            location=location,
                                                            desc=desc,
                                                            updateuserid=updateuserid,
                                                            updatetime=ToMysqlDateTimeNow(),
                                                            isdel=isdel)
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


# BloodRrlation
async def BloodRrlationInsOrUp(request):
    form = await request.json()
    beid = form.get('beid')
    srcid = form.get('srcid')
    dstid = form.get('dstid')
    relation = form.get('relation')
    isdel = form.get('isdel', 1)
    try:

        if beid and isdel == 1:  # update
            effectrows = await BloodEdge(beid=beid,
                                         srcid=srcid,
                                         dstid=dstid,
                                         relation=relation,
                                         isdel=isdel
                                         ).upd()
        elif not beid:  # create
            effectrows = await BloodEdge(beid=next_id(),
                                         srcid=srcid,
                                         dstid=dstid,
                                         relation=relation,
                                         isdel=isdel
                                         ).save()
        elif beid and isdel == 0:  # delete
            effectrows = await BloodEdge(beid=beid).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# MetaDataClass
async def MetaDataClassInsOrUp(request):
    form = await request.json()
    id = form.get('mcid')
    pid = form.get('pid')
    metaclsno = form.get('metaclsno')
    classno = form.get('classno')
    isresource = form.get('isresource')
    level = form.get('level')
    metaclsname = form.get('metaclsname')
    metaclspy = form.get('metaclspy')
    remark = form.get('remark')
    app = form.get('app')
    createname = form.get('createname')
    isdel = form.get('isdel', 1)
    try:

        if id and isdel == 1:  # update
            effectrows = await MetaDataClass(mcid=id).upd2(isresource=isresource,
                                                           metaclsname=metaclsname,
                                                           metaclspy=metaclspy,
                                                           remark=remark,
                                                           app=app,
                                                           createname=createname)
        elif not id:  # create
            effectrows = await MetaDataClass(mcid=next_id(),
                                             pid=pid,
                                             metaclsno=metaclsno,
                                             classno=classno,
                                             isresource=isresource,
                                             level=level,
                                             metaclsname=metaclsname,
                                             metaclspy=metaclspy,
                                             remark=remark,
                                             app=app,
                                             createname=createname,
                                             isdel=isdel
                                             ).save()
        elif id and isdel == 0:  # delete
            effectrows = await MetaDataClass(mcid=id).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# MetaData
async def MetaDataInsOrUp(request):
    form = await request.json()
    id = form.get('metaid')
    mcid = form.get('metaclsid')
    resourceno = form.get('standardno')
    standardno = form.get('standardno')
    metaname = form.get('metaname')
    metapy = form.get('metapy')
    columnname = form.get('columnname')
    oldcolumnname = form.get('oldcolumnname')
    columntype = form.get('columntype')
    columnlen = form.get('columnlen')
    metadefine = form.get('metadefine')
    remark = form.get('remark')
    createuserid = form.get('createuserid')
    isdel = form.get('isdel', 1)
    try:

        if id and isdel == 1:  # update
            effectrows = await MetaData(metaid=id).upd2(resourceno=resourceno,
                                                        standardno=standardno,
                                                        metaname=metaname,
                                                        metapy=metapy,
                                                        columnname=columnname,
                                                        oldcolumnname=oldcolumnname,
                                                        columntype=columntype,
                                                        columnlen=columnlen,
                                                        metadefine=metadefine,
                                                        remark=remark,
                                                        updateuserid=createuserid,
                                                        updatetime=ToMysqlDateTimeNow())
        elif not id:  # create
            effectrows = await MetaData(metaid=next_id(),
                                        mcid=mcid,
                                        resourceno=resourceno,
                                        standardno=standardno,
                                        metaname=metaname,
                                        metapy=metapy,
                                        columnname=columnname,
                                        oldcolumnname=oldcolumnname,
                                        columntype=columntype,
                                        columnlen=columnlen,
                                        metadefine=metadefine,
                                        remark=remark,
                                        createuserid=createuserid,
                                        createtime=ToMysqlDateTimeNow(),
                                        isdel=isdel
                                        ).save()
        elif id and isdel == 0:  # delete
            effectrows = await MetaData(metaid=id).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def MetaDataDelete(request):
    """
    :param request:
    :return:
    """
    form = await request.json()
    id = form.get('id')
    # id = request.query.get('id')
    if (not id):
        data = dict(failure=True, data="find no id!")
        return render_json(data)
    try:
        effectrows = await MetaData(metaid=id).rm()
        if effectrows >= 1:
            data = dict(success=True, data=effectrows)
        else:
            data = dict(failure=True, data='delete fuilure!')
        return render_json(data)
    except Exception as e:
        data = dict(failure=True, data=str(e))
        return render_json(data)


# NosqlDatabase
async def NosqlDatabaseInsOrUp(request):
    form = await request.json()
    id = form.get('ndid')
    dbname = form.get('name')
    describe = form.get('describe')
    ip = form.get('ip')
    port = form.get('port')
    accountnumber = form.get('accountnumber')
    password = form.get('password')
    remark = form.get('remark')
    createuserid = form.get('createuserid ')
    updateuserid = form.get('updateuserid ')
    isdel = form.get('isdel', 1)
    print(form)
    try:

        if id and isdel == 1:  # update
            effectrows = await NosqlDatabase(ndid=id).upd2(dbname=dbname,
                                                           describe=describe,
                                                           ip=ip,
                                                           port=port,
                                                           accountnumber=accountnumber,
                                                           password=password,
                                                           remark=remark,
                                                           updateuserid=updateuserid,
                                                           updatetime=ToMysqlDateTimeNow(),
                                                           isdel=isdel)
        elif not id:  # create
            effectrows = await NosqlDatabase(ndid=next_id(),
                                             dbname=dbname,
                                             describe=describe,
                                             ip=ip,
                                             port=port,
                                             accountnumber=accountnumber,
                                             password=password,
                                             remark=remark,
                                             createuserid=createuserid,
                                             createtime=ToMysqlDateTimeNow(),
                                             isdel=isdel
                                             ).save()
            gfs = GFS(dbname=dbname)
            await gfs.init()

        elif id and isdel == 0:  # delete
            effectrows = await NosqlDatabase(ndid=id).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# TableColumn
async def DBTableColumnInsOrUp(request):
    form = await request.json()
    id = form.get('colid')
    tabid = form.get('tabid')
    metaid = form.get('metaid')
    ispk = form.get('ispk')
    isnull = form.get('isnull')
    isuq = form.get('isuq')
    range = form.get('range')
    isdel = form.get('isdel', 1)
    try:

        if id and isdel == 1:  # update
            effectrows = await DBTableColumn(colid=id).upd2(ispk=ispk,
                                                            isnull=isnull,
                                                            isuq=isuq,
                                                            range=range,
                                                            isdel=isdel)
        elif not id:  # create
            effectrows = await DBTableColumn(colid=next_id(),
                                             tabid=tabid,
                                             metaid=metaid,
                                             ispk=ispk,
                                             isnull=isnull,
                                             isuq=isuq,
                                             range=range,
                                             isdel=isdel
                                             ).save()
        elif id and isdel == 0:  # delete
            effectrows = await DBTableColumn(colid=id).upd2(isdel=0)

        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# TableColumndel
async def DBTableColumnBatchDel(request):
    form = await request.json()
    batchid = form.get('batchid')
    print(str(batchid))
    print(type(str(batchid)))
    x = re.search(r'^\[(.*?)\]$', str(batchid))
    # print(x.group())
    # print(x.group(1))
    try:
        sql = f'delete from dbtablecolumn where colid in ({x.group(1)})'

        print(sql)
        effectrows = await orm.execute(sql=sql, args=())
        logging.info(effectrows)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


# endregion


# region nosql mongodb

async def testUploadFile(request):
    print(request)
    form = await request.post()
    form = dict(**form)
    img = form.get('file').file
    image = img.read()
    print(image)
    print(img)
    print(form)

    Url = request.message
    content = request.content
    x = request.query_string
    y = await content.read()
    # z = await request.post()
    # m = await request.json()
    print(Url)
    print(y)
    print(x)
    with open('test.png', 'wb') as f:
        f.write(image)


async def UploadFile(request):
    """
    use: action=http://127.0.0.1:9000/api/v1/UploadFile
    :param request:
    :return:
    """
    form = await request.post()
    form = dict(**form)
    DBName = request.query.get('DBName')
    file = form.get('file')
    print(file)
    namelist = file.filename.split('.')
    filename = namelist[:-1][0]
    file = file.file
    # content_type = file.content_type
    image = file.read()
    try:
        gfs = GFS(dbname=DBName)
        effectrows = await gfs.putBytes(bytes=image, name=filename)
        data = dict(success=True, data=effectrows)
        return render_json(data)
    except Exception as e:
        logging.error(e)
        data = dict(failure=True, data=str(e))
        return render_json(data)


async def GetImage(request):
    """
    use: http://127.0.0.1:9000/api/v1/GetImage?FileID=xxxxxxxxxxxxxxx
    :param request:
    :return:
    """
    # form = await request.post()
    DBName = request.query.get('DBName')
    FileID = request.query.get('FileID')
    gfs = GFS(dbname=DBName)
    # x,y = gfs.get('5ae3d6299f6b8f1714c7fdb5')
    x, y = await gfs.get(FileID)
    # print(x)
    # print(y)
    return render_image(x)


async def NosqlQuery(request):
    """
    example x = gfs.find(query={"filename": "1.png"}, projection={"filename":1}).sort([('uploadDate', -1)]).limit(1)
    :param reqest:
    :return:
    """
    DBName = request.query.get('DBName')
    FileName = request.query.get('FileName')
    CurrentPage = request.query.get('CurrentPage')
    PageSize = request.query.get('PageSize')
    print(FileName)
    if FileName:
        query = {"filename": {'$regex': FileName}}  # '$regex' 模糊查询
    else:
        query = None
    print(query)
    gfs = GFS(dbname=DBName)
    # res = gfs.find(query={"filename": FileName}, projection={"chunkSize": 0}).sort([('uploadDate', -1)]).skip(int(CurrentPage)).limit(int(PageSize))
    # reslist = list(res)
    if (not CurrentPage or not PageSize):
        data = dict(failure=True, data="find no parameters CurrentPage or PageSize !")
        return render_json(data)
    else:
        try:
            num = await gfs.find(query=query).count()

            p = Page(num, int(CurrentPage), int(PageSize))  # totalcount  # currentpage  # pagesize
            if num == 0:
                data1 = dict(page=p.GetDict, res=[])
            else:
                # list = await VDBTable.findAll(limit=(p.offset, p.limit))
                reslist = await gfs.find(query=query, projection={"chunkSize": 0})\
                                .sort([('uploadDate', -1)])\
                                .skip(p.offset)\
                                .limit(p.limit)\
                                .to_list(length=100)

                reslistmap = list(map(lambda x: {"_id": str(x['_id']),
                                                 "filename": x['filename'],
                                                 "format": x.get("format", ""),
                                                 "uploadDate": str(x['uploadDate']),
                                                 "length": round(x['length'] / 1024 / 1024, 2)}, reslist))

                data1 = dict(page=p.GetDict, res=reslistmap)
            data = dict(success=True, data=data1)
            return render_json(data)
        except Exception as e:
            data = dict(failure=True, data=e)
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


# region ggg


# endregion
