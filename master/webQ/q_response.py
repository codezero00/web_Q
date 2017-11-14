# from aiohttp.web_response import *
from aiohttp.web_response import Response as rq
from aiohttp import web
from aiohttp.helpers import (sentinel)
import json


class Response(rq):
    '''
    继承自aiohttp.web_response 的 Response
    '''
    pass


def json_response(data=sentinel, *, text=None, body=None, status=200,
                  reason=None, headers=None, content_type='application/json',
                  dumps=json.dumps):
    if data is not sentinel:
        if text or body:
            raise ValueError(
                "only one of data, text, or body should be specified"
            )
        else:
            text = dumps(data)
    return Response(text=text, body=body, status=status, reason=reason,
                      headers=headers, content_type=content_type)
