from utils.db import get_connection

class BaseDAO:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()
