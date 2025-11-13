from dao.user_dao import UserDAO
user_dao = UserDAO()

class UserService:
    @staticmethod
        def list_users():
                return [u.to_dict() for u in user_dao.list_all()]

                    @staticmethod
                        def get_user(user_id):
                                u = user_dao.get_by_id(user_id)
                                        return u.to_dict() if u else None

                                            @staticmethod
                                                def update_user(user_id, data):
                                                        user = user_dao.update(user_id, **data)
                                                                return user.to_dict()

                                                                    @staticmethod
                                                                        def delete_user(user_id):
                                                                                return user_dao.delete(user_id)
                                                                                