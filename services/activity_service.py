from dao.activity_dao import ActivityDAO
activity_dao = ActivityDAO()

class ActivityService:
    @staticmethod
    def create_activity(user_id, title, description=None):
        a = activity_dao.create(user_id, title, description)
        return a.to_dict()

    @staticmethod
    def list_activities():
        return [a.to_dict() for a in activity_dao.list_all()]

    @staticmethod
    def list_by_user(user_id):
        return [a.to_dict() for a in activity_dao.list_by_user(user_id)]

    @staticmethod
    def get_activity(aid):
        a = activity_dao.get_by_id(aid)
        return a.to_dict() if a else None

    @staticmethod
    def update_activity(aid, data):
        a = activity_dao.update(aid, **data)
        return a.to_dict()

    @staticmethod
    def delete_activity(aid):
        return activity_dao.delete(aid)
