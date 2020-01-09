import sqlite3
import hashlib
import random
import argparse

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

def compute_n_hashings(string, n):
    for i in range(n):
        string = hashlib.sha256(string.encode('utf-8')).hexdigest()
    return string
    
def insert_user(user_id, password):
    global conn
    global cursor
    salt = random.randint(1, 50)
    password = str(salt) + password
    digest = compute_n_hashings(password, 100)
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (user_id, digest, salt))
    conn.commit()


def remove_user(user_id, password):
    global conn
    global cursor
    cursor.execute("DELETE FROM users WHERE username = ?", (user_id,))
    conn.commit()
    
def parse_arguments():
    parser = argparse.ArgumentParser(
            description="Process user intention (add or remove new user")
            
    parser.add_argument("action", choiches = ['add','remove'],
                        help="Add or remove user")

    parser.add_argument('-u', help="user id", required=True, default=None)
    parser.add_argument('-p', help="user password",
                        required=False, default=None)
    args = parser.parse_args()
    return args


