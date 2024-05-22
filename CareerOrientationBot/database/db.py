from aiomysql import Pool, Cursor
from asyncio import exceptions
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
                
#Добавление професии 
    async def insert_prof(self, telegram_id, prof_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("UPDATE users SET profession = %s WHERE telegram_id = %s", (prof_id, telegram_id))
                await conn.commit()
                
#Поиск професси по категории
    async def select_prof(self, prof_category):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("SELECT * FROM professions WHERE prof_category = %s", prof_category)
                await conn.commit()
                return await cur.fetchall()

#Поиск професси по id
    async def select_prof_byId(self, prof_id):
        async with self.pool.acquire() as conn:
            async with conn.cursor(Cursor) as cur:
                await cur.execute("SELECT * FROM professions WHERE prof_id = %s", prof_id)
                await conn.commit()
                return await cur.fetchall()