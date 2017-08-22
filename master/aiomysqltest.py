import asyncio, logging
import aiomysql
import sys


async def create_pool(loop):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(host='127.0.0.1',
                                        port=3306,
                                        user='root',
                                        password='zhangjun',
                                        db='gold',
                                        loop=loop)


# 销毁连接池
async def destory_pool():
    global __pool
    if __pool is not None:
        __pool.close()
        await __pool.wait_closed()


async def test_example():
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            await cur.close()
            print(r)
            assert r == 42
    __pool.close()
    await __pool.wait_closed()


# sql文日志输出
def log(sql, args=()):
    logging.info('SQL：%s' % sql)


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('row returned：%s' % len(rs))
        return rs


async def my_test(loop):
    await create_pool(loop=loop)
    x = await test_example()
    return x




loop = asyncio.get_event_loop()
loop.run_until_complete(my_test(loop))


