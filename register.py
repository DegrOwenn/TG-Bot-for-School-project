import sqlite3

class Users:

    #Базовый инит
    def __init__(self, users_file):
        self.connection = sqlite3.connect(users_file)
        self.cursor = self.connection.cursor()

    #Добавление пользователя
    def new_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users ('user_id') VALUES (?)", (user_id,))

    #Проверяет, есть ли уже пользователь
    def exists_or_not(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    #Указка имени
    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id,))
        
    #На какой стадии регистра находится пользователь
    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT sign_up FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                sign_up = str(row[0])
            return sign_up
        
    #Изменение этапа регистра пользователя
    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET sign_up = ? WHERE user_id = ?", (signup, user_id,))

    #В каком городе находится пользователь
    def set_city(self, user_id, city):
        with self.connection:
            self.cursor.execute("UPDATE users SET city = ? WHERE user_id = ?", (city, user_id,))
            return 'Запомнили'
        
    def get_city(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT city FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                city = str(row[0])
            return city

    #Расписание присыла
    def set_schedule(self, user_id, schedule):
        with self.connection:
            self.cursor.execute("UPDATE users SET schedule = ? WHERE user_id = ?", (schedule, user_id,))
            return 'Запомнили'

    def get_schedule(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT schedule FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                schedule = str(row[0])
            return schedule
        
    def reset_schedule(self, user_id, schedule):
        with self.connection:
            self.cursor.execute("UPDATE users SET schedule = ? WHERE user_id = ?", (schedule, user_id,))
            return 'Сброшено. Теперь вам не будут приходить увдеомления в назначенное время'