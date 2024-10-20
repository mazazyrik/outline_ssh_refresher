import logging

import sqlite3

logging.basicConfig(level=logging.INFO)


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('your_database.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (ids INTEGER PRIMARY KEY)'''
        )

        self.conn.commit()
        logging.info('Connected to SQLite database successfully')

    def save_id(self, id: int) -> None:
        '''
        This method saves id in ids column.
        '''
        self.cursor.execute('''INSERT INTO users (ids) VALUES (%s)''', (id,))
        self.conn.commit()
        logging.info(f'{id} saved to db.')

    def get_ids(self) -> set[int]:
        '''
        This method returns all ids in the database as a set.
        '''
        self.cursor.execute('''SELECT ids FROM users''')
        rows = self.cursor.fetchall()
        return {row[0] for row in rows}

    def close(self):
        self.cursor.close()
        self.conn.close()
