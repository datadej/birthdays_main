import sqlite3
import hashlib
import random

conn = None
cursor = None


def open_create(db_path):
    global conn
    global cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
    except sqlite3.OperationalError:
        create_users_table()


def create_users_table():
    global conn
    global cursor
    cursor.execute('''CREATE TABLE users
                   (id VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt INT NOT NULL,
                    PRIMARY KEY (id))''')

def insert_user(user_id, password):
    global conn
    global cursor
    salt = random.randint(1, 50)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (user_id, digest, salt))
    conn.commit()


def remove_user(user_id, password):
    global conn
    global cursor
    cursor.execute("DELETE FROM users WHERE username = ?", (user_id,))
    conn.commit()