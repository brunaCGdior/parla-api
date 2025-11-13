from dao.character_dao import CharacterDAO
character_dao = CharacterDAO()

class CharacterService:
    @staticmethod
        def create_character(user_id, name, avatar=None):
                c = character_dao.create(user_id, name, avatar)
                        return c.to_dict()

                            @staticmethod
                                def list_characters():
                                        return [c.to_dict() for c in character_dao.list_all()]

                                            @staticmethod
                                                def list_by_user(user_id):
                                                        return [c.to_dict() for c in character_dao.list_by_user(user_id)]

                                                            @staticmethod
                                                                def get_character(cid):
                                                                        c = character_dao.get_by_id(cid)
                                                                                return c.to_dict() if c else None

                                                                                    @staticmethod
                                                                                        def update_character(cid, data):
                                                                                                c = character_dao.update(cid, **data)
                                                                                                        return c.to_dict()

                                                                                                            @staticmethod
                                                                                                                def delete_character(cid):
                                                                                                                        return character_dao.delete(cid)
                                                                                                                        