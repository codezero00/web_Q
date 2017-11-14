import hashlib
import time
import logging

_COOKIE_NAME = 'AKEELAH'
_COOKIE_KEY = 'AKKKKKKKK!@#'

class LoginManager(object):
    '''
    登陆类
    '''

    def __init__(self):
        self.user_callback = None

    def init_app(self, app):
        '''
        将class LoginManager 实例传入 webQ实例，定义实例为login_manager
        :param app:
        :return:
        '''
        app.login_manager = self

    def user_loader(self, callback):
        '''
        回调装饰器，将账号查询函数传给实例的user_callback参数
        :param callback: The callback for retrieving a user object.
        :type callback: callable
        '''
        self.user_callback = callback
        return callback

    # 解密cookie:
    async def cookie2user(self, cookie_str):
        '''
        Parse cookie and load user if cookie is valid.
        '''
        if not cookie_str:
            return None
        try:
            L = cookie_str.split('-')
            if len(L) != 3:
                return None
            uid, expires, sha1 = L
            if int(expires) < time.time():
                return None
            user = await self.user_callback(uid)
            logging.info('user : %s' % (user))
            if user is None:
                return None
            s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
            if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
                logging.info('invalid sha1')
                return None
            user.passwd = '******'
            return user
        except Exception as e:
            logging.exception(e)
            return None



# 计算加密cookie:
def encode_cookie(user, max_age):
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

# 解密cookie:
async def decode_cookie(cookie_str, callback):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        # user = await User.find(uid)
        user = callback(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None