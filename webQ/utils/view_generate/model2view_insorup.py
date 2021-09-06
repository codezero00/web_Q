import webQ.utils.cache.cache_model as model  # 这里注意要引入需要生成的model
from jinja2 import Template, Environment, FileSystemLoader
from webQ.utils.config import *

def get_model_attr():
    """
    通过model.py 文件获取class属性 返回 table_name pri_key cloumns
    :return:
    """
    model_dict = model.__dict__

    class_list = list(filter(lambda x: str(type(x[1])) == "<class 'webQ.q_orm.ModelMetaclass'>", model_dict.items()))[
                 1:]

    tables = []
    for k, v in class_list:
        table_name = k
        q = dict(v.__dict__)
        pri_key = q['__primary_key__']
        columns = q['__fields__']
        # print(f'{table_name}:{pri_key}:{columns}')
        table = dict(table_name=table_name, pri_key=pri_key, columns=[x for x in columns if x !='createtime' and x !='updatetime'])
        tables.append(table)
    dict_string = dict(tables=tables)
    return dict_string


def read_template(dict_string):
    """
    :param dict_string: {'models_string':xxxx}
    :return:
    """
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template('view_insorup.template')
    genmodel = template.render(dict_string)
    return genmodel


def run():
    dict_string = get_model_attr()
    # with open('../generated_file/myview_insorup.py', 'w', encoding='utf8') as f:
    #     f.write(read_template(dict_string=dict_string))
    with open(os.path.join(file_path, 'gen_view_insorup.py'), 'w', encoding='utf8') as f:
        f.write(read_template(dict_string=dict_string))

if __name__ == '__main__':
    run()
