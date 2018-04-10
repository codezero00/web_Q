# from aiohttp.web_response import *
from aiohttp.web_response import Response as rq
from aiohttp import web,http_websocket
from aiohttp.helpers import (sentinel)
import json
from enum import IntEnum

class Response(rq):
    '''
    继承自aiohttp.web_response 的 Response
    '''
    pass

class WebSocketResponse(web.WebSocketResponse):
    '''
    继承自aiohttp.web.WebSocketResponse 的 WebSocketResponse
    '''
    pass

class WSMsgType(IntEnum):
    # websocket spec types
    CONTINUATION = 0x0
    TEXT = 0x1
    BINARY = 0x2
    PING = 0x9
    PONG = 0xa
    CLOSE = 0x8

    # aiohttp specific types
    CLOSING = 0x100
    CLOSED = 0x101
    ERROR = 0x102

    text = TEXT
    binary = BINARY
    ping = PING
    pong = PONG
    close = CLOSE
    closing = CLOSING
    closed = CLOSED
    error = ERROR

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

def render_json(data):
    res = Response()
    res.content_type = 'application/json'
    res.body = json.dumps(data, ensure_ascii=False).encode('utf-8')
    return res