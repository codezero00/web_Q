from webq import webQ
import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os
from aiohttp import web
import urls
from orm import create_pool

app = webQ(urls.urlpatterns)




if __name__ == '__main__':
    app.run()