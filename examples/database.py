import sqlite3


def create_schema(db_path="circle.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            line_user_id TEXT UNIQUE,
            role TEXT NOT NULL DEFAULT 'member'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS collections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount INTEGER NOT NULL,
            deadline TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            collection_id INTEGER NOT NULL,
            member_id INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'unpaid',
            paid_amount INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (collection_id) REFERENCES collections(id),
            FOREIGN KEY (member_id) REFERENCES members(id)
        )
    """)

    conn.commit()
    conn.close()
