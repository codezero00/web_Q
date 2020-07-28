from jinja2 import Template, Environment, FileSystemLoader
from webQ.utils.config import *


def read_template():
    """
    :param dict_string: {'models_string':xxxx}
    :return:
    """
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template('del_gen.template')
    genmodel = template.render()
    return genmodel


def run():
    with open(os.path.join(file_path, '修改文件名称(去掉gen).bat'), 'w', encoding='utf8') as f:
        f.write(read_template())

if __name__ == '__main__':
    run()
