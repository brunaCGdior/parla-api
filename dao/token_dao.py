from .base_dao import BaseDAO
from models.token_blocklist import TokenBlocklist

class TokenDAO(BaseDAO):
    def add(self, jti):
            self.cur.execute("INSERT INTO token_blocklist (jti) VALUES (?)", (jti,))
                    self.conn.commit()
                            return True

                                def exists(self, jti):
                                        self.cur.execute("SELECT * FROM token_blocklist WHERE jti = ?", (jti,))
                                                row = self.cur.fetchone()
                                                        return True if row else False
                                                        