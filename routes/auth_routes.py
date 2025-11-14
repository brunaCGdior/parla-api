from flask import Blueprint, request, jsonify
from services.auth_service import AuthService, bcrypt
from utils.responses import ok, created, error
from flask_jwt_extended import jwt_required, get_jwt, create_access_token, get_jwt_identity
from dao.token_dao import TokenDAO

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
token_dao = TokenDAO()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    try:
        user = AuthService.register(data["username"], data["email"], data["password"])
        return created(user.to_dict())
    except ValueError as ve:
        if str(ve) == "username_taken":
            return error("Username already taken", 400)
        if str(ve) == "email_taken":
            return error("Email already taken", 400)
    except Exception as e:
        return error("Registration error: " + str(e), 500)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    res = AuthService.login(data.get("username") or data.get("email"), data["password"])
    if not res:
        return error("Invalid credentials", 401)
    return ok({"access_token": res["access_token"], "user": res["user"].to_dict()}, "Logged in")

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token_dao.add(jti)
    return ok(msg="Logged out")
