from flask import Blueprint, request
from services.auth_service import AuthService
from utils.responses import ok, created, client_error, unauthorized, server_error
from utils.validators import is_valid_email, is_valid_password, required_fields
from flask_jwt_extended import jwt_required, get_jwt
from dao.token_dao import TokenDAO

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
token_dao = TokenDAO()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    missing = required_fields(data, ["username", "email", "password"])
    if missing:
        return client_error("Missing required fields", "missing_fields", errors={"missing": missing})
    if not is_valid_email(data["email"]):
        return client_error("Invalid email format", "invalid_email")
    if not is_valid_password(data["password"], min_len=8):
        return client_error("Password too short (min 8 chars)", "weak_password")
    try:
        user = AuthService.register(data["username"], data["email"], data["password"])
        return created(user.to_dict(), "User created", "user_created")
    except ValueError as ve:
        msg = str(ve)
        if msg == "username_taken":
            return client_error("Username already taken", "username_taken")
        if msg == "email_taken":
            return client_error("Email already taken", "email_taken")
        return client_error("Registration error", "registration_error", errors={"detail": msg})
    except Exception as e:
        return server_error("Unexpected server error", "server_error")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    missing = required_fields(data, ["password"])
    if missing:
        return client_error("Missing required fields", "missing_fields", errors={"missing": missing})
    username_or_email = data.get("username") or data.get("email")
    if not username_or_email:
        return client_error("Provide username or email", "missing_identity")
    res = AuthService.login(username_or_email, data["password"])
    if not res:
        return unauthorized("Invalid credentials", "invalid_credentials")
    return ok({"access_token": res["access_token"], "user": res["user"].to_dict()}, "Logged in", "logged_in")

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_dao.add(jti)
    return ok(msg="Logged out", data=None, code="logged_out")
