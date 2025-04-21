import sqlite3
import os

DB_PATH = os.path.join("data", "journal.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            content TEXT,
            mood TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_journal_entry(date, content, mood):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO entries (date, content, mood)
        VALUES (?, ?, ?)
    ''', (date, content, mood))
    conn.commit()
    conn.close()

# Initialize the DB on first import
init_db()
