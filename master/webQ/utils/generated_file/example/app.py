# from webq import webQ
import os
import logging

logging.basicConfig(level=logging.INFO)
from webQ.webq import webQ
from urls import urlpatterns

__HOST = os.environ['HOST']
__DATABASE = os.environ['DATABASE']
__USER = os.environ['USER']
__PASSWORD = os.environ['PASSWORD']

# __HOST = '172.16.4.110'
# __DATABASE = 'ncp'
# __USER = 'root'
# __PASSWORD = 'zyjs2018!'


cors_urls = tuple(x[0] for x in urlpatterns)


app = webQ(urlpatterns)
app.conf_multiports = (7001, 7002, 7003, 7004)  # 多进程
app.conf_cors_url = "*"  # 允许跨域的域名
# app.conf_cors_routes = ('name11', 'name13', 'login', 'reg', 'islogin', 'metaclasstree', 'metaclass')
app.conf_cors_routes = cors_urls  # 所有url跨域

app.conf_dbsource = dict(
    host=__HOST,
    port=3306,
    user=__USER,
    password=__PASSWORD,
    db= __DATABASE
)

# app.conf_others = dict(
#     static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
#     templates_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# )

app.conf_swagger = dict(
    # swagger_from_file='swagger.yaml'
    swagger_url='/api/v1/doc'
)

'''
如果需要启用登陆验证相关功能，请取消以下注释
'''
# from webQ.q_login import LoginManager
# from model import SYS_USERS

# def init_login():
#     # 实例化LoginManager 类
#     login_manager = LoginManager()
#     # 将实例login_manager 传入到app 实例，并定义为app.login_manager
#     login_manager.init_app(app)

#     # Create user loader function
#     # 装饰器将load_user函数传入到login_manager实例的user_callback参数
#     @login_manager.user_loader
#     async def load_user(uid):
#         try:
#             # return await User.find(1)
#             return await SYS_USERS.find(uid)
#         except:
#             return None


# init_login()


async def helloworld(request):
    """
    ---
    description: init！
    tags:
    - hello world!
    produces:
    - application/json
    """
    return "helloworld!!"

if __name__ == '__main__':
    app.run(7000)
    # app.multi_run()
