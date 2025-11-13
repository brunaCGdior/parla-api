from .base_dao import BaseDAO
from models.user import UserModel

class UserDAO(BaseDAO):
    def create(self, username, email, password):
            try:
                        self.cur.execute(
                                        "INSERT INTO users (username, email, password) VALUES (?,?,?)",
                                                        (username, email, password)
                                                                    )
                                                                                self.conn.commit()
                                                                                            user_id = self.cur.lastrowid
                                                                                                        return self.get_by_id(user_id)
                                                                                                                except Exception as e:
                                                                                                                            raise e

                                                                                                                                def get_by_id(self, id):
                                                                                                                                        self.cur.execute("SELECT * FROM users WHERE id = ?", (id,))
                                                                                                                                                row = self.cur.fetchone()
                                                                                                                                                        return UserModel(**row) if row else None

                                                                                                                                                            def get_by_username(self, username):
                                                                                                                                                                    self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
                                                                                                                                                                            row = self.cur.fetchone()
                                                                                                                                                                                    return UserModel(**row) if row else None

                                                                                                                                                                                        def get_by_email(self, email):
                                                                                                                                                                                                self.cur.execute("SELECT * FROM users WHERE email = ?", (email,))
                                                                                                                                                                                                        row = self.cur.fetchone()
                                                                                                                                                                                                                return UserModel(**row) if row else None

                                                                                                                                                                                                                    def list_all(self):
                                                                                                                                                                                                                            self.cur.execute("SELECT * FROM users")
                                                                                                                                                                                                                                    rows = self.cur.fetchall()
                                                                                                                                                                                                                                            return [UserModel(**r) for r in rows]

                                                                                                                                                                                                                                                def update(self, id, **kwargs):
                                                                                                                                                                                                                                                        fields = []
                                                                                                                                                                                                                                                                values = []
                                                                                                                                                                                                                                                                        for k, v in kwargs.items():
                                                                                                                                                                                                                                                                                    fields.append(f"{k} = ?")
                                                                                                                                                                                                                                                                                                values.append(v)
                                                                                                                                                                                                                                                                                                        values.append(id)
                                                                                                                                                                                                                                                                                                                sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
                                                                                                                                                                                                                                                                                                                        self.cur.execute(sql, tuple(values))
                                                                                                                                                                                                                                                                                                                                self.conn.commit()
                                                                                                                                                                                                                                                                                                                                        return self.get_by_id(id)

                                                                                                                                                                                                                                                                                                                                            def delete(self, id):
                                                                                                                                                                                                                                                                                                                                                    self.cur.execute("DELETE FROM users WHERE id = ?", (id,))
                                                                                                                                                                                                                                                                                                                                                            self.conn.commit()
                                                                                                                                                                                                                                                                                                                                                                    return self.cur.rowcount > 0
                                                                                                                                                                                                                                                                                                                                                                    