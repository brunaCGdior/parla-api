import sqlite3
from config import Config

def get_connection():
    conn = sqlite3.connect(Config.DATABASE, check_same_thread=False)
        conn.row_factory = sqlite3.Row
            return conn

            def init_db():
                conn = get_connection()
                    cur = conn.cursor()

                        # users
                            cur.execute("""
                                CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                username TEXT UNIQUE NOT NULL,
                                                        email TEXT UNIQUE NOT NULL,
                                                                password TEXT NOT NULL,
                                                                        created_at TEXT DEFAULT CURRENT_TIMESTAMP
                                                                            )
                                                                                """)

                                                                                    # activities (1:N user -> activities)
                                                                                        cur.execute("""
                                                                                            CREATE TABLE IF NOT EXISTS activities (
                                                                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                                                            user_id INTEGER NOT NULL,
                                                                                                                    title TEXT NOT NULL,
                                                                                                                            description TEXT,
                                                                                                                                    status TEXT DEFAULT 'pending',
                                                                                                                                            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                                                                                                                                                    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                                                                                                                                                        )
                                                                                                                                                            """)

                                                                                                                                                                # characters (personagens) (1:N user -> characters)
                                                                                                                                                                    cur.execute("""
                                                                                                                                                                        CREATE TABLE IF NOT EXISTS characters (
                                                                                                                                                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                                                                                                                                        user_id INTEGER NOT NULL,
                                                                                                                                                                                                name TEXT NOT NULL,
                                                                                                                                                                                                        avatar TEXT,
                                                                                                                                                                                                                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                                                                                                                                                                                                                        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                                                                                                                                                                                                                            )
                                                                                                                                                                                                                                """)

                                                                                                                                                                                                                                    # token blocklist (for logout)
                                                                                                                                                                                                                                        cur.execute("""
                                                                                                                                                                                                                                            CREATE TABLE IF NOT EXISTS token_blocklist (
                                                                                                                                                                                                                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                                                                                                                                                                                                            jti TEXT NOT NULL,
                                                                                                                                                                                                                                                                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                                            """)

                                                                                                                                                                                                                                                                                conn.commit()
                                                                                                                                                                                                                                                                                    conn.close()
                                                                                                                                                                                                                                                                                    