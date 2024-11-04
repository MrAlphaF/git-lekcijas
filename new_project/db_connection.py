import mysql.connector
import json

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Connect to the database
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)

cursor = db.cursor()
cursor.execute("SELECT * FROM my_table")
for row in cursor.fetchall():
    print(row)

db.close()
