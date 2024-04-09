
import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (ids INTEGER)''')


def save_id(id: int) -> None:
    cursor.execute('''INSERT INTO users (ids) VALUES (?)''', (id,))
    conn.commit()


def get_ids() -> list[int]:
    cursor.execute('''SELECT ids FROM users''')
    rows = cursor.fetchall()
    return rows
