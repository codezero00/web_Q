
import json, time, hashlib, logging
import webQ.q_orm  as orm
from webQ.q_response import Response, json_response
from webQ.q_login import _COOKIE_NAME, encode_cookie
from webQ.q_helpers import _RE_EMAIL, _RE_SHA1, APIValueError, APIError, next_id
import model
from model import User

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
    if user.passwd != sha1.hexdigest():
        raise Exception('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = Response()
    # r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400, httponly=True)
    r.set_cookie(_COOKIE_NAME, encode_cookie(user, 86400), max_age=86400)
    user.passwd = '******'
    r.content_type = 'application/json'
    data = dict()
    data['success'] = True
    data['data'] = user
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

async def islogin(request):
    if request.__user__:
        ##
        data = dict()
        data['success'] = True
        #data4['failure'] = None
        data['data'] = request.__user__
        ##
        r = Response()
        # request.__user__.passwd = '******'
        r.content_type = 'application/json'
        r.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        # r.body = json.dumps(request.__user__, ensure_ascii=False).encode('utf-8')
        return r
    else:
        raise APIError('do not login! plase login!')