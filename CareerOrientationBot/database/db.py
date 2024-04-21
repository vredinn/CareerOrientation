from aiomysql import Pool, Cursor
import sqlite3
from asyncio import exceptions
import config
from database.connect import db_connect

class Database():
    pool: Pool = db_connect

#Поиск пользователя по TG ID
    async def select_user(self, telegram_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("SELECT * FROM users WHERE telegram_id = %s", telegram_id)
                await conn.commit()
                return await cur.fetchone()
    
#Добавление пользвователя 
    async def insert_user(self, user_name, user_phone, telegram_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("INSERT INTO users (user_name, user_phone, telegram_id) VALUES (%s, %s, %s)", (user_name, user_phone, telegram_id))
                await conn.commit()
        
#Удаление пользователя
    async def delete_user(self, telegram_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("DELETE FROM users WHERE telegram_id = %s", telegram_id)
                await conn.commit()