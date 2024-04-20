from asyncio import exceptions
import sqlite3
class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()
        
#Создание таблицы users
    def create_db(self):
        try:
            query = ("CREATE TABLE users ("
	                 "user_id INTEGER NOT NULL UNIQUE, "
	                 "user_name TEXT NOT NULL, "
	                 "user_phone TEXT NOT NULL, "
	                 "telegram_id INTEGER NOT NULL, "
	                 "PRIMARY KEY(user_id AUTOINCREMENT));")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Ошибка при создании:", Error)
            
#Поиск пользователя по TG ID
    def select_user(self, telegram_id):
        users =self.cursor.execute(f"SELECT * FROM users WHERE telegram_id = {telegram_id}")
        return users.fetchone()
    
#Добавление пользвователя 
    def add_user(self, user_name, user_phone, telegram_id ):
        self.cursor.execute(f"INSERT INTO users (user_name, user_phone, telegram_id) VALUES ('{user_name}','{user_phone}', {telegram_id})")
        self.connection.commit()
        
#Удаление пользователя
    def delete_user(self, telegram_id):
        self.cursor.execute(f"DELETE FROM users WHERE telegram_id = {telegram_id}")
        self.connection.commit()
        
#Закрытие соединения
    def __del__(self):
        self.cursor.close()
        self.connection.close()