def run_migration():
    cursor.execute("CREATE TABLE IF NOT EXISTS your_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    db.commit()

run_migration()
