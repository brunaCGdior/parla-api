from dao.user_dao import UserDAO

user_dao = UserDAO()

class UserService:

    @staticmethod
    def get_all():
        return user_dao.get_all()

    @staticmethod
    def get_by_id(user_id):
        return user_dao.get_by_id(user_id)

    @staticmethod
    def get_by_email(email):
        return user_dao.get_by_email(email)

    @staticmethod
    def update(user_id, data):
        user = user_dao.get_by_id(user_id)
        if not user:
            return None
        updated = user_dao.update(user_id, data)
        return updated

    @staticmethod
    def delete(user_id):
        return user_dao.delete(user_id)
