import logging
logging.basicConfig(level=logging.INFO)

import orm
import asyncio, json, os
from aiohttp import web
from jinja2 import Environment, FileSystemLoader


class webQ(object):
    def __init__(self,
                 patterns=None
                 ):
        self.patterns = patterns

    def init_jinja2(self, app, **kw):
        logging.info('init jinja2...')
        options = dict(
            autoescape = kw.get('autoescape', True),
            block_start_string = kw.get('block_start_string', '{%'),
            block_end_string = kw.get('block_end_string', '%}'),
            variable_start_string = kw.get('variable_start_string', '{{{'),
            variable_end_string = kw.get('variable_end_string', '}}}'),
            auto_reload = kw.get('auto_reload', True)
        )
        path = kw.get('path', None)
        if path is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        logging.info('set jinja2 template path: %s' % path)
        env = Environment(loader=FileSystemLoader(path), **options)
        filters = kw.get('filters', None)
        if filters is not None:
            for name, f in filters.items():
                env.filters[name] = f
        app['__templating__'] = env


    async def logger_factory(self, app, handler):
        async def logger(request):
            logging.info('request from: %s,%s' %
                         (request.method, request.path))
            return await handler(request)
        return logger

    async def response_factory(self, app, handler):
        '''
        中间件
        '''
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
                    resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                    resp.content_type = 'application/json;charset=utf-8'
                    return resp
                else:
                    resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                    resp.content_type = 'text/html;charset=utf-8'
                    return resp
            # if isinstance(r, int) and r >= 100 and r < 600:
            #     return web.Response(r)
            # if isinstance(r, tuple) and len(r) == 2:
            #     t, m = r
            #     if isinstance(t, int) and t >= 100 and t < 600:
            #         return web.Response(t, str(m))
            # default:
            resp = web.Response(body=str(r).encode('utf-8'))
            resp.content_type = 'text/plain;charset=utf-8'
            return resp
        return response

    def add_url_rule(self, app, method, path, view_func=None):
        logging.info('add_url_rule : {} {} call funcation: {} '.format(method,path,view_func.__name__) )
        app.router.add_route(method, path, view_func)

    def add_static(self,app):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        app.router.add_static('/static/', path)
        logging.info('add static %s => %s' % ('/static/', path))

    def setup_routes(self, app, patterns):
        for attr in patterns:
            #logging.info('func_name: %s' % str(attr))
            _method = attr[0]
            _path = attr[1]
            _fnc1 = attr[2]
            n = _fnc1.split('.')
            _module = n[-2]
            _fuc2 = n[-1]
            weqapp = __import__(_module)
            _fuc3 = getattr(weqapp,_fuc2)
            self.add_url_rule(app, method=_method, path=_path, view_func=_fuc3)

    async def setup(self, loop):
        await orm.create_pool(loop=loop)   ### 创建数据库连接池
        app = web.Application(loop=loop, middlewares=[self.logger_factory,self.response_factory])
        self.init_jinja2(app)
        self.add_static(app)
        self.setup_routes(app, self.patterns)
        srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
        logging.info('server started at http://127.0.0.1:9000...')
        return srv

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.setup(loop))
        loop.run_forever()


# if __name__ == '__main__':
#     main()
    # for attr in dir(view):
    #     logging.info('func_name: %s' % str(attr))
