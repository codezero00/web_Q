from aiohttp import web
import json, time
import orm
import logging


def index(request):
    return web.Response(body=u'<h1>hello word</h1>')


def index1(request):
    data = {
        '__template__': 'index.html',
        'data': '...'
    }
    # if isinstance(data,dict):
    #     rep=web.Response(body=app[__])
    return web.Response(body=u'<h1>hello word1111111111</h1>')


def index2(request):
    url_param = request.match_info['gid']
    print(request)
    print(url_param)
    return web.Response(body=u'<h1>hello word！ {},{}</h1>'.format(request, url_param))


def index3(request):
    data = {
        'id': '1',
        'name': 'akeec',
        'desc': '啊哈哈哈'
    }
    return web.json_response(data)


def index4(request):
    data = {
        'id': '2222',
        'name': 'akeec',
        'desc': 'okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
    }
    rep = web.Response()
    rep.set_cookie('P_UID', 'AGASGLKSAEG', max_age=86400, httponly=True)
    rep.content_type = 'application/json'
    rep.body = (json.dumps(data, ensure_ascii=False).encode('utf-8'))
    # rep.body = (u'<h1>hello word1111111111</h1>')
    return rep


def index5(request):
    mysql = "SELECT 42;"
    print(mysql)
    list = orm.select1(mysql=mysql)
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
        '__template__': 'blog.html',
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
    通过连接池完成mysql查询
    :param request:
    :return:
    '''
    logging.info('get int index8')
    list = await orm.exec()
    print('endddddddddddddd{}'.format(str(list)))
    return str(list)