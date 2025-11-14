from .base_dao import BaseDAO
from models.activity import ActivityModel

class ActivityDAO(BaseDAO):
    def create(self, user_id, title, description, status="pending"):
        self.cur.execute(
            "INSERT INTO activities (user_id, title, description, status) VALUES (?,?,?,?)",
            (user_id, title, description, status)
        )
        self.conn.commit()
        return self.get_by_id(self.cur.lastrowid)

    def get_by_id(self, id):
        self.cur.execute("SELECT * FROM activities WHERE id = ?", (id,))
        row = self.cur.fetchone()
        return ActivityModel(**row) if row else None

    def list_all(self):
        self.cur.execute("SELECT * FROM activities")
        rows = self.cur.fetchall()
        return [ActivityModel(**r) for r in rows]

    def list_by_user(self, user_id):
        self.cur.execute("SELECT * FROM activities WHERE user_id = ?", (user_id,))
        rows = self.cur.fetchall()
        return [ActivityModel(**r) for r in rows]

    def update(self, id, **kwargs):
        fields = []
        values = []
        for k, v in kwargs.items():
            fields.append(f"{k} = ?")
            values.append(v)
        values.append(id)
        sql = f"UPDATE activities SET {', '.join(fields)} WHERE id = ?"
        self.cur.execute(sql, tuple(values))
        self.conn.commit()
        return self.get_by_id(id)

    def delete(self, id):
        self.cur.execute("DELETE FROM activities WHERE id = ?", (id,))
        self.conn.commit()
        return self.cur.rowcount > 0
