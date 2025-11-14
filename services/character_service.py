from dao.character_dao import CharacterDAO

char_dao = CharacterDAO()

class CharacterService:

    @staticmethod
    def create(user_id, data):
        return char_dao.create(user_id, data["name"], data.get("avatar"))

    @staticmethod
    def get_all():
        return char_dao.get_all()

    @staticmethod
    def get_by_user(user_id):
        return char_dao.get_by_user(user_id)

    @staticmethod
    def get_by_id(char_id):
        return char_dao.get_by_id(char_id)

    @staticmethod
    def update(char_id, data):
        char = char_dao.get_by_id(char_id)
        if not char:
            return None
        return char_dao.update(char_id, data)

    @staticmethod
    def delete(char_id):
        return char_dao.delete(char_id)
