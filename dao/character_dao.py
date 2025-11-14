from .base_dao import BaseDAO
from models.character import CharacterModel

class CharacterDAO(BaseDAO):
    def create(self, user_id, name, avatar=None):
        self.cur.execute(
            "INSERT INTO characters (user_id, name, avatar) VALUES (?,?,?)",
            (user_id, name, avatar)
        )
        self.conn.commit()
        return self.get_by_id(self.cur.lastrowid)

    def get_by_id(self, id):
        self.cur.execute("SELECT * FROM characters WHERE id = ?", (id,))
        row = self.cur.fetchone()
        return CharacterModel(**row) if row else None

    def list_all(self):
        self.cur.execute("SELECT * FROM characters")
        rows = self.cur.fetchall()
        return [CharacterModel(**r) for r in rows]

    def list_by_user(self, user_id):
        self.cur.execute("SELECT * FROM characters WHERE user_id = ?", (user_id,))
        rows = self.cur.fetchall()
        return [CharacterModel(**r) for r in rows]

    def update(self, id, **kwargs):
        fields = []
        values = []
        for k, v in kwargs.items():
            fields.append(f"{k} = ?")
            values.append(v)
        values.append(id)
        sql = f"UPDATE characters SET {', '.join(fields)} WHERE id = ?"
        self.cur.execute(sql, tuple(values))
        self.conn.commit()
        return self.get_by_id(id)

    def delete(self, id):
        self.cur.execute("DELETE FROM characters WHERE id = ?", (id,))
        self.conn.commit()
        return self.cur.rowcount > 0
