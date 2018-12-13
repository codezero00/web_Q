import webQ.utils.generated_file.mymodel_view as model  # 这里注意要引入需要生成的model
from jinja2 import Template, Environment, FileSystemLoader


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
        table = dict(table_name=table_name, pri_key=pri_key, columns=columns)
        tables.append(table)
    dict_string = dict(tables=tables)
    return dict_string


def read_template(dict_string):
    """
    :param dict_string: {'models_string':xxxx}
    :return:
    """
    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('view_query_detail.template')
    genmodel = template.render(dict_string)
    return genmodel


def run():
    dict_string = get_model_attr()
    with open('../generated_file/myview_query_detail.py', 'w', encoding='utf8') as f:
        f.write(read_template(dict_string=dict_string))


if __name__ == '__main__':
    run()
