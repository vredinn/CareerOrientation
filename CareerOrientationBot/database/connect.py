import aiomysql
import config
import asyncio
from app.loader import loop


# Подключение к БД
async def connect(loop):
    return await aiomysql.create_pool(host=config.host,
                                      port=3306,
                                      user=config.user,
                                      password=config.password,
                                      db=config.db,
                                      loop = loop
    )

db_connect = loop.run_until_complete(connect(loop))