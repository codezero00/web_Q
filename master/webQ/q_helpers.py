import time
import uuid
import re
import datetime

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


def ToMysqlDateTimeNow():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt


class Page(object):

    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count  # 总数
        self.page_size = page_size  # 没叶多少条
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        if (item_count == 0) or (page_index > self.page_count):
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            self.page_index = page_index
            self.offset = self.page_size * (page_index - 1)
            self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1

    def __str__(self):
        return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (
        self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)

    __repr__ = __str__

    @property
    def GetDict(self):
        return dict(item_count=self.item_count, page_count=self.page_count, page_index=self.page_index,
                    page_size=self.page_size, offset=self.offset, limit=self.limit)


class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''

    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''

    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)


def ColumnCheck(filter_str, fields):
    """
    校验where条件数据 检测参数是否存在，防止SQL注入
    :param filter_str: 'a=1 and b in 2 and c like 3 or d=4 or e=5'
    :param fields: class instance fields
    :return: True or False
    """
    filter_str = filter_str.lower()
    conditions = re.split(' and | or ', filter_str)
    columns = list(map(lambda x: re.split('=|!=|<>| in | like |>|< ', x)[0].strip(), conditions))
    judge_set = set(map(lambda x: x.strip() in fields, columns))
    if False in judge_set:
        return False
    else:
        return True