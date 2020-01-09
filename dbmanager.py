import sqlite3
import hashlib

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