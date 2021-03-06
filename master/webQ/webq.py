import logging

logging.basicConfig(level=logging.INFO)

from .q_orm import *
import asyncio
import json
import os
from aiohttp import web
import aiohttp_cors
from jinja2 import Environment, FileSystemLoader
from multiprocessing import Pool
from .q_helpers import *
from .q_login import _COOKIE_NAME, _COOKIE_KEY, decode_cookie, LoginManager
from functools import wraps

from aiohttp_swagger import *


class webQ(object):
    def __init__(self, patterns=None):
        self.patterns = patterns
        self._others = {}
        self._dbsource = None
        self._portlist = None
        self._cors_url = None
        self._cors_routes = None
        self._swagger_conf = {}
        self._permission_request_func = None

    def init_jinja2(self, app, **kw):
        logging.info('init jinja2...')
        options = dict(
            autoescape=kw.get('autoescape', True),
            # block_start_string=kw.get('block_start_string', '{%'),
            # block_end_string=kw.get('block_end_string', '%}'),
            # variable_start_string=kw.get('variable_start_string', '{{'),
            # variable_end_string=kw.get('variable_end_string', '}}'),
            auto_reload=kw.get('auto_reload', True)
        )
        path = kw.get('templates_path', None)
        if path is None:
            path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'templates')
        logging.info('set jinja2 template path: %s' % path)
        env = Environment(loader=FileSystemLoader(path), **options)
        filters = kw.get('filters', None)
        if filters is not None:
            for name, f in filters.items():
                env.filters[name] = f
        app['__templating__'] = env

    """
    工厂模式
    """

    async def logger_factory(self, app, handler):
        async def logger(request):
            logging.info('request from: %s,%s' %
                         (request.method, request.path))
            return await handler(request)

        return logger

    async def response_factory(self, app, handler):
        """
        中间件
        """

        async def response(request):
            logging.info('Response handler...')
            r = await handler(request)
            if isinstance(r, web.StreamResponse):
                return r
            if isinstance(r, bytes):
                resp = web.Response(body=r)
                resp.content_type = 'application/octet-stream'
                return resp
            if isinstance(r, str):
                if r.startswith('redirect:'):
                    return web.HTTPFound(r[9:])
                resp = web.Response(body=r.encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
            if isinstance(r, dict):
                template = r.get('__template__')
                if template is None:
                    resp = web.Response(body=json.dumps(
                        r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                    resp.content_type = 'application/json;charset=utf-8'
                    return resp
                else:
                    resp = web.Response(body=app['__templating__'].get_template(
                        template).render(**r).encode('utf-8'))
                    resp.content_type = 'text/html;charset=utf-8'
                    return resp
            resp = web.Response(body=str(r).encode('utf-8'))
            resp.content_type = 'text/plain;charset=utf-8'
            return resp

        return response

    async def auth_factory(self, app, handler):
        async def auth(request):
            logging.info('check user: %s %s' % (request.method, request.path))
            request.__user__ = None
            cookie_str = request.cookies.get(_COOKIE_NAME)
            if cookie_str:
                user = await self.login_manager.cookie2user(cookie_str)
                if user:
                    logging.info('set current user: %s' % user.email)
                    request.__user__ = user
                    request.__user__.passwd = '******'
                    logging.info('current urser auth_factory !!!! = {}'.format(user))
            return (await handler(request))

        return auth


    def permission_request(self, callback):
        self._permission_request_func= callback
        return callback

    async def permission_factory(self, app, handler):
        """
        true pass /false nopass rv为True则通过，否则不通过 await handler(request) 触发view（放后面表示before_request 前面表示after_request）
        :param app:
        :param handler:
        :return:
        """
        async def wrapper(request):
            func = self._permission_request_func
            rv = True
            if func:
                rv =await func(request)
            if not rv:
                content = json.dumps(dict(code=403, message=str('Permission denied !'), data=""), ensure_ascii=False).encode('utf-8')
                resp = web.Response(body=content)
                resp.content_type = 'text/json;charset=utf-8'
                return resp
            else:
                return await handler(request)
        return wrapper

    """
    class function
    """

    def init_swagger(self, app, **kwargs):
        logging.info('init swagger...')
        # if not kwargs:
        #     raise ValueError('init_swagger kwargs can not be None')
        swagger_from_file = kwargs.get('swagger_from_file', None)
        swagger_url = kwargs.get('swagger_url', None)
        setup_swagger(app=app, swagger_from_file=swagger_from_file, swagger_url=swagger_url, api_base_url='/')
        logging.info('init swagger successful...')

    def add_url_rule(self, app, method, path, name, view_func=None):
        logging.info('add_url_rule : {} {} call funcation: {} '.format(
            method, path, view_func.__name__))
        app.router.add_route(method, path, view_func, name=name)

    def add_static(self, app, **kw):
        path = kw.get('static_path', None)
        if path is not None:
            # path = os.path.join(os.path.dirname(
            #     os.path.abspath(__file__)), 'static')
            app.router.add_static('/static/', path)
            logging.info('add static %s => %s' % ('/static/', path))
        else:
            logging.info('you do not set static floder path')

    def setup_routes(self, app, patterns):
        for attr in patterns:
            # logging.info('func_name: %s' % str(attr))
            _name = attr[0]
            _method = attr[1]
            _path = attr[2]
            _fnc1 = attr[3]
            n = _fnc1.split('.')
            _module = n[-2]
            _fuc2 = n[-1]
            """
            __import__ python内置函数
            1. 函数功能用于动态的导入模块，主要用于反射或者延迟加载模块。
            2. __import__(module)相当于import module
            
            返回 对象obj module
            
            getattr(object, name[, default])
            
            getattr() 函数用于返回一个对象属性值。
            
            
            """
            weqapp = __import__(_module)
            _fuc3 = getattr(weqapp, _fuc2)
            self.add_url_rule(app, method=_method, path=_path,
                              view_func=_fuc3, name=_name)

    async def setup(self, loop, port):
        # await orm.create_pool(loop=loop)   ### 创建数据库连接池
        if self._dbsource is not None:
            await create_pool(loop=loop, **self._dbsource)  # 创建数据库连接池
        app = web.Application(loop=loop, middlewares=[self.logger_factory, self.permission_factory, self.response_factory, self.auth_factory])
        app['sockets'] = []
        self.init_jinja2(app, **self._others)
        self.add_static(app, **self._others)
        self.setup_routes(app, self.patterns)

        # Configure CORS on all routes. 配置所有router都可以跨域（配置touter name=name13 , name11 的router的可以跨域）
        cors = self.aio_cors(app)
        cors_routes = filter(
            lambda x: x.name in self._cors_routes, list(app.router.routes()))
        for route in cors_routes:
            cors.add(route)

        # 注册url到swagger,必须放在add_router 后面
        self.init_swagger(app=app, **self._swagger_conf)

        # 端口
        srv = await loop.create_server(app.make_handler(), '0.0.0.0', port)
        logging.info('server started at http://0.0.0.0: %s ...' % (port))
        return srv

    def aio_cors(self, app, **kw):
        """
        aio_http不支持跨域，这是是跨域插件
        """
        # Configure default CORS settings.
        cors = aiohttp_cors.setup(app, defaults={
            self._cors_url: aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        })
        return cors

    def run(self, port):
        """
        单进程
        :param port:
        :return:
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.setup(loop, port))
        loop.run_forever()

    def multi_run(self):
        """
        多进程
        :return:
        """
        print('Parent process %s.' % os.getpid())
        # p = Pool(3)
        # for i in (9000,9001,9002):
        #     p.apply_async(self.run, args=(i,))
        p = Pool(len(self._portlist))
        for i in self._portlist:
            p.apply_async(self.run, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')

    """
    Python内置的@property装饰器就是负责把一个方法变成属性调用的
    """

    @property
    def conf_multiports(self):
        return self._portlist

    @conf_multiports.setter
    def conf_multiports(self, value):
        if not isinstance(value, tuple):
            raise ValueError('conf_multiports must be tuple!')
        self._portlist = value

    @property
    def conf_cors_url(self):
        return self._cors_url

    @conf_cors_url.setter
    def conf_cors_url(self, value):
        if not isinstance(value, str):
            raise ValueError('conf_cors_url must be str!')
        self._cors_url = value

    @property
    def conf_cors_routes(self):
        return self._cors_routes

    @conf_cors_routes.setter
    def conf_cors_routes(self, value):
        if not isinstance(value, tuple):
            raise ValueError('conf_cors_routes must be tuple!')
        self._cors_routes = value

    @property
    def conf_dbsource(self):
        return self._dbsource

    @conf_dbsource.setter
    def conf_dbsource(self, value):
        if value and not isinstance(value, dict):
            raise ValueError('conf_dbsource must be dict!')
        self._dbsource = value

    @property
    def conf_others(self):
        return self._others

    @conf_others.setter
    def conf_others(self, value):
        if not isinstance(value, dict):
            raise ValueError('conf_others must be dict!')
        self._others = value

    @property
    def conf_swagger(self):
        """
        可以不用提前定义 _swagger_conf
        :return:
        """
        return self._swagger_conf

    @conf_swagger.setter
    def conf_swagger(self, value):
        """
        python版本getter,setter  动态给class赋值~ 必须先用setter 赋值，然后getter
        :param value: dict
        :return: dict
        """
        if not isinstance(value, dict):
            raise ValueError('conf_swagger must be dict!')
        self._swagger_conf = value
