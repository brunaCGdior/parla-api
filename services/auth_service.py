from dao.user_dao import UserDAO
from dao.token_dao import TokenDAO
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt
from datetime import datetime, timedelta

user_dao = UserDAO()
token_dao = TokenDAO()
bcrypt = Bcrypt()

class AuthService:
    @staticmethod
    def register(username, email, password):
        if user_dao.get_by_username(username):
            raise ValueError("username_taken")
        if user_dao.get_by_email(email):
            raise ValueError("email_taken")
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        user = user_dao.create(username, email, hashed)
        return user

    @staticmethod
    def login(username_or_email, password):
        user = user_dao.get_by_username(username_or_email) or user_dao.get_by_email(username_or_email)
        if not user:
            return None
        if not bcrypt.check_password_hash(user.password, password):
            return None
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "user": user}

    @staticmethod
    def logout(jti):
        token_dao.add(jti)
