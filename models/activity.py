class ActivityModel:
    def __init__(self, id, user_id, title, description, status, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }
