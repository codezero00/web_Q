import asyncio, logging

import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', '127.0.0.1'),
        port=kw.get('port', 3306),
        user='root', #kw['user','root'],
        password='zhangjun', #kw['password','zhangjun'],
        db='gold', #kw['db','gold'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select1(mysql):
    print('it is in!!!!')
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(mysql)
            print(cur.description)
            (r,) = await cur.fetchone()
            await cur.close()
            logging.info('rows returned: %s' % len(r))
            return r


async def test_example():
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            await cur.close()
            print(r)
            return r

async def exec():
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:
            SQL="""
            select
            t2.code,
            t2.name,
            t2.industry,
            t1.today,
            t1.yesterday,
            t1.tod_high,
            t1.tod_low,
            t1.yes_high,
            t1.yes_low,
            t1.gaptype,
            t1.gapdesc
            from (
            SELECT *
            FROM gold.gap order by today desc limit 1,10) t1
            left join sharelist t2 on t1.code=t2.code
            """
            await cur.execute(SQL)
            print(cur.description)
            r = await cur.fetchall()
            await cur.close()
            print(r)
            return r