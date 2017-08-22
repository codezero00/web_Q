# import logging,inspect,asyncio,os
# from aiohttp import web


# class webq_urls(object):
#     def __init__(self, app):
#         self._app = app
#         #self._func = fn

#     async def __call__(self, request):
#         kw = None
#         r = await self._func(**kw)
#         return r

#     @classmethod
#     def add_route(app, method, path, fn):
#         if path is None or method is None:
#             raise ValueError('@get or @post not defined in %s.' % str(fn))
#         if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
#             fn = asyncio.coroutine(fn)
#         logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
#         app.router.add_route(method, path, fn)

#     @classmethod
#     def add_route2(app, method, path, fn):
#         if path is None or method is None:
#             raise ValueError('@get or @post not defined in %s.' % str(fn))
#         if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
#             fn = asyncio.coroutine(fn)
#         logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
#         app.router.add_route(method, path, fn)

#     @classmethod
#     def setup_routes(app,module_name):
#         for attr in dir(module_name):
#             logging.info('func_name: %s' % str(attr))
            