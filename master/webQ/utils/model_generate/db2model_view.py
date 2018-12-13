import asyncio
import aiomysql
import logging
# import aiofiles
from jinja2 import Template, Environment, FileSystemLoader


async def create_pool(loop, **kw):
    """
    创建连接池
    :param loop:
    :param kw:
    :return:
    """
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', '172.16.4.110'),
        port=kw.get('port', 3306),
        user=kw.get('user', 'root'),
        password=kw.get('password', 'zyjs2018!'),
        db=kw.get('db', ''),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


async def select(p_sql, param):
    """
    execute your sql what's input
    :param p_sql:
    :param param:
    :return:
    """
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:
            SQL = p_sql
            await cur.execute(SQL, param)
            r = await cur.fetchall()
            return r


async def gettable(table_schema):
    """
    xxx
    :return:
    """
    sql = """
    select TABLE_NAME from INFORMATION_SCHEMA.TABLES where table_schema=%s and table_type = 'VIEW'
    """
    result = await select(p_sql=sql, param=(table_schema))
    return result


async def getmodel(table_schema, table_name):
    """
    xxx
    :return:
    """
    sql = f"""
    select concat("class ",upper(table_name),"(Model):") as orm_head
    from INFORMATION_SCHEMA.TABLES
    where table_name='{table_name}' and table_schema='{table_schema}'
    union all
    select concat("	__table__ = '",table_name,"'") as orm_mid
    from INFORMATION_SCHEMA.TABLES
    where table_name='{table_name}' and table_schema='{table_schema}'
    union all
    select concat("	",column_name, 
    case when column_key='PRI' then " = StringField(primary_key=True,ddl='varchar(200)')" 
    else " = StringField(ddl='varchar(200)')" end) as orm_body
    from INFORMATION_SCHEMA.COLUMNS
    where table_name='{table_name}' and table_schema='{table_schema}'
    """
    result = await select(p_sql=sql, param=())
    return result


async def example_test(loop):
    await create_pool(loop=loop)
    result = await select(p_sql='select * from dbtable where remark= %s', param=('测试表四00'))
    print(result)


def read_template(dict_string):
    """
    :param dict_string: {'models_string':xxxx}
    :return:
    """
    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('model.template')
    genmodel = template.render(dict_string)
    return genmodel
    # with open('model.template', 'r') as f:
    #     template_string = f.read()
    # model_temlplate = Template(template=template_string)
    # genmodel = model_temlplate.substitute(dict_string)
    # return genmodel


async def run(loop):
    table_schema = 'zyjs_dwc_20181101'

    await create_pool(loop=loop, kw={'db': table_schema})  # 创建连接池

    table_name_list = await gettable(table_schema=table_schema)
    models_string = ''
    for table_name in table_name_list:
        '''
        获取table name 然后循环获取列
        '''
        models = await getmodel(table_schema=table_schema, table_name=table_name[0])
        for model_row in models:
            '''
            获取列 然后循环拼接model字符
            '''
            models_string += model_row[0] + '\n'
        models_string += '\n\n'
    dict_string = dict(models_string=models_string)
    print(dict_string)
    with open('../generated_file/mymodel_view.py', 'w', encoding='utf8') as f:
        f.write(read_template(dict_string=dict_string))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # loop.run_until_complete(example_test(loop=loop))

    loop.run_until_complete(run(loop=loop))
