# main.py

import mysql.connector
import json

# Load configuration from file
with open('config.json') as config_file:
    config = json.load(config_file)

# Establish database connection
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)

def read_data():
    
    #Function to read data from the database
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM your_table")
    for row in cursor.fetchall():
        print(row)

    db.close()

def run_migration():
    
    #Function to run database migration
    
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS your_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    db.commit()

# Running migration
run_migration()

# Reading data
read_data()
