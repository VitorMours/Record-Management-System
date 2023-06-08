import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "informacao_clientes"

def restart_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(f"UPDATE sqlite_sequence SET seq=1 WHERE {TABLE_NAME}")


def create(NEW_TABLE_NAME):
    global TABLE_NAME
    TABLE_NAME = f"{NEW_TABLE_NAME}"
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {NEW_TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT)")
    connection.commit()
    connection.close()

def insert(value,value2):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO {TABLE_NAME} (nome, sobrenome) VALUES (?,?)", (value,value2))
    connection.commit()
    connection.close()

def fetch_data():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    values = data.fetchall()
    connection.commit()
    connection.close()
    return values

def fetch_last_id():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    id = cursor.execute(f"SELECT id FROM {TABLE_NAME} ORDER BY id DESC ")
    last_id = id.fetchone()[0]
    connection.commit()
    connection.close()
    return last_id
    



if __name__ == "__database__":
    restart_database()