import subprocess

def backup_database():
    subprocess.run(['pg_dump', 'mydatabase', '-f', 'backup.sql'])

backup_database()
