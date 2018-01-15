# from webq import webQ
import os
import logging

logging.basicConfig(level=logging.INFO)
from webQ.webq import webQ
from webQ.q_login import LoginManager
from model import User
from urls import urlpatterns

app = webQ(urlpatterns)
app.conf_multiports = (9001, 9002, 9003, 9004)
app.conf_cors_url = "*"
app.conf_cors_routes = ('name11', 'name13', 'login', 'reg', 'islogin')
app.conf_dbsource = dict(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='zhangjun',
    db='akeec'
)
app.conf_others = dict(
    static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
    templates_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
)


def init_login():
    # 实例化LoginManager 类
    login_manager = LoginManager()
    # 将实例login_manager 传入到app 实例，并定义为app.login_manager
    login_manager.init_app(app)

    # Create user loader function
    # 装饰器将load_user函数传入到login_manager实例的user_callback参数
    @login_manager.user_loader
    async def load_user(uid):
        try:
            # return await User.find(1)
            return await User.find(uid)
        except:
            return None


init_login()

if __name__ == '__main__':
    app.run(9000)
    # app.multi_run()
