import sqlite3

DB_NAME = "worklog.db"


def get_connection():
    """
    SQLite の接続を返す
    """
    return sqlite3.connect(DB_NAME)


def init_db():
    """
    DB 初期化
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
