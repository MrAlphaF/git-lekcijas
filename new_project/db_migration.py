import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

def migrate_table():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''ALTER TABLE users ADD COLUMN email TEXT''')
    conn.commit()
    conn.close()

create_table()
migrate_table()

