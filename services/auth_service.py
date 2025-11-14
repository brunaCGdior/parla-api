from dao.user_dao import UserDAO
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from utils.validators import is_valid_email

bcrypt = Bcrypt()
user_dao = UserDAO()

class AuthService:

    @staticmethod
    def register(username, email, password):
        # check duplicates
        if user_dao.get_by_username(username):
            raise ValueError("username_taken")
        if user_dao.get_by_email(email):
            raise ValueError("email_taken")

        hashed = bcrypt.generate_password_hash(password).decode("utf-8")
        user = user_dao.create(username, email, hashed)
        return user

    @staticmethod
    def login(username_or_email, password):
        # accept username or email
        if is_valid_email(username_or_email):
            user = user_dao.get_by_email(username_or_email)
        else:
            user = user_dao.get_by_username(username_or_email)

        if not user:
            return None

        if not bcrypt.check_password_hash(user.password, password):
            return None

        token = create_access_token(identity=user.id)
        return {
            "access_token": token,
            "user": user
        }
