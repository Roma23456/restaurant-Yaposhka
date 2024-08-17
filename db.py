import sqlite3

def init_db():
    conn = sqlite3.connect('hotels.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS busket (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_hotel(name, description, price):
    conn = sqlite3.connect('hotels.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO restaurant (name, description, price) VALUES (?, ?, ?)
    ''', (name, description, price))
    conn.commit()
    conn.close()


init_db()