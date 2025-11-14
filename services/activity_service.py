from dao.activity_dao import ActivityDAO

activity_dao = ActivityDAO()

class ActivityService:

    @staticmethod
    def create(user_id, data):
        return activity_dao.create(user_id, data["title"], data.get("description"))

    @staticmethod
    def get_all():
        return activity_dao.get_all()

    @staticmethod
    def get_by_user(user_id):
        return activity_dao.get_by_user(user_id)

    @staticmethod
    def get_by_id(activity_id):
        return activity_dao.get_by_id(activity_id)

    @staticmethod
    def update(activity_id, data):
        activity = activity_dao.get_by_id(activity_id)
        if not activity:
            return None
        return activity_dao.update(activity_id, data)

    @staticmethod
    def delete(activity_id):
        return activity_dao.delete(activity_id)
