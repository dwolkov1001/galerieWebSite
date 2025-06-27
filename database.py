import sqlite3
from datetime import datetime
import os

DATABASE_PATH = 'database.db'

def init_db():
    """Инициализация базы данных и создание таблиц"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE,
            password_hash TEXT NOT NULL
        )
    ''')
    # Таблица изображений с user_id
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            caption TEXT,
            upload_date DATETIME NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("База данных инициализирована успешно!")

def get_db_connection():
    """Получение соединения с базой данных"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к столбцам по имени
    return conn

def add_image(filename, caption, user_id):
    """Добавление нового изображения в базу данных"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images (filename, caption, upload_date, user_id)
        VALUES (?, ?, ?, ?)
    ''', (filename, caption, datetime.now(), user_id))
    image_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return image_id

def get_all_images():
    """Получение всех изображений из базы данных"""
    conn = get_db_connection()
    images = conn.execute('SELECT * FROM images ORDER BY upload_date DESC').fetchall()
    conn.close()
    return images

def delete_image(image_id):
    """Удаление изображения из базы данных"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Получаем информацию об изображении перед удалением
    image = cursor.execute('SELECT * FROM images WHERE id = ?', (image_id,)).fetchone()
    
    if image:
        # Удаляем запись из базы данных
        cursor.execute('DELETE FROM images WHERE id = ?', (image_id,))
        conn.commit()
        conn.close()
        return image
    
    conn.close()
    return None

def get_image_by_id(image_id):
    """Получение информации об изображении по id"""
    conn = get_db_connection()
    image = conn.execute('SELECT * FROM images WHERE id = ?', (image_id,)).fetchone()
    conn.close()
    return image

# --- Пользователи ---
def add_user(username, email, password_hash):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                       (username, email, password_hash))
        conn.commit()
        user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        user_id = None
    conn.close()
    return user_id

def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def update_user_password(user_id, new_password_hash):
    conn = get_db_connection()
    conn.execute('UPDATE users SET password_hash = ? WHERE id = ?', (new_password_hash, user_id))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Инициализация базы данных при запуске файла напрямую
    init_db() 