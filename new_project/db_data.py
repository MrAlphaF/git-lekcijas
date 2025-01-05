import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert a row of data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Save (commit) the changes
conn.commit()

# Read data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
