import os
templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')

from webQ.utils.config import *

if __name__ == '__main__':
    __model_path = os.path.join(model_path, 'db2model.py')
    __model_view_path = os.path.join(model_path, 'db2model_view.py')
    __url_path = os.path.join(view_path, 'model2url.py')
    __batch_ins_path = os.path.join(view_path, 'model2view_batch_ins.py')
    __del_path = os.path.join(view_path, 'model2view_del.py')
    __insorup_path = os.path.join(view_path, 'model2view_insorup.py')
    __query_detail_path = os.path.join(view_path, 'model2view_query_detail.py')
    __query_page_path = os.path.join(view_path, 'model2view_query_page.py')
    __query_tree_path = os.path.join(view_path, 'model2view_query_tree.py')
    ## 修改文件名的批处理文件
    __bat_del_gen = os.path.join(view_path, 'bat_del_gen.py')

    os.system(f'python {__model_path}')
    os.system(f'python {__model_view_path}')

    os.system(f'python {__batch_ins_path}')
    os.system(f'python {__del_path}')
    os.system(f'python {__insorup_path}')
    os.system(f'python {__query_detail_path}')
    os.system(f'python {__query_page_path}')
    os.system(f'python {__query_tree_path}')
    os.system(f'python {__url_path}')
    ## 修改文件名的批处理文件
    os.system(f'python {__bat_del_gen}')

    # print(templates_path)
    # print(os.listdir(templates_path))