"""
Database config
可配置项
"""

# HOST = '172.16.4.110'
# PORT = 3306
# USER = 'root'
# PASSWORD = 'zyjs2018!'
# SCHEMA = 'zyjs_dwc_20181101'

# HOST = '172.16.4.112'
# PORT = 3306
# USER = 'root'
# PASSWORD = 'zyjs123ZYJS'
# SCHEMA = 'qydb'

HOST = '172.16.4.110'
PORT = 3306
USER = 'root'
PASSWORD = 'zyjs2018!'
SCHEMA = 'zyjs_dwc_20181101'


"""
Generated path
可配置项(默认generated_file文件夹)
"""


# GEN_PATH = 'C:/Users/Administrator/Desktop/webq_meta_tmp'

GEN_PATH = 'C:/Users/Administrator/Desktop/wdis_backend/gen'


"""
Path
非配置项
"""

import os

templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model_generate')
view_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'view_generate')
cache_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')

if not GEN_PATH:
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generated_file')
else:
    file_path = GEN_PATH

# print(os.path.join(file_path, 'mymodel.py'))