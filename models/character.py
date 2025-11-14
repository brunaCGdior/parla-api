class CharacterModel:
    def __init__(self, id, user_id, name, avatar, created_at):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.avatar = avatar
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "avatar": self.avatar,
            "created_at": self.created_at
        }
