import os
import sqlite3

class Database():
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

# Unit Test
if __name__ == '__main__':
    # Get dbPath
    dbpath = os.path.join(os.getcwd(), os.path.pardir, 'data', 'test.db')
    print('dbpath = {}'.format(dbpath))
    # Instantiate a database object
    db = Database(dbpath)
    # Insert data
    db.cursor.execute('drop table test')
    db.cursor.execute('create table test(id CHAR(8) PRIMARY KEY, name VARCHAR(20))')
    db.cursor.execute('insert into test values(?, ?)', ('08291094', 'helyao'))
    db.cursor.execute('insert into test values(?, ?)', ('12125070', 'helyao'))
    # Select data
    db.cursor.execute('select * from test where id = ?', ('08291094',))
    results = db.cursor.fetchall()
    print(results)
    db.cursor.execute('select * from test where name = ?', ('helyao',))
    results = db.cursor.fetchall()
    print(results)
