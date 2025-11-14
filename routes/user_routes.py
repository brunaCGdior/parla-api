from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import UserService
from utils.responses import ok, created, client_error, unauthorized, not_found
from utils.validators import required_fields, is_valid_email

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("", methods=["GET"])
@jwt_required()
def list_users():
    users = UserService.get_all()
    return ok([u.to_dict() for u in users], "Users listed", "users_listed")


@user_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return not_found("User not found", "user_not_found")
    return ok(user.to_dict(), "User retrieved", "user_retrieved")


@user_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    data = request.get_json() or {}

    # check user exists
    user = UserService.get_by_id(user_id)
    if not user:
        return not_found("User not found", "user_not_found")

    # only the user themselves can edit
    current = get_jwt_identity()
    if current != user_id:
        return unauthorized("You cannot edit another user", "forbidden_action")

    # validate fields
    if "email" in data and not is_valid_email(data["email"]):
        return client_error("Invalid email format", "invalid_email")

    updated = UserService.update(user_id, data)
    return ok(updated.to_dict(), "User updated", "user_updated")


@user_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    user = UserService.get_by_id(user_id)
    if not user:
        return not_found("User not found", "user_not_found")

    current = get_jwt_identity()
    if current != user_id:
        return unauthorized("You cannot delete another user", "forbidden_action")

    UserService.delete(user_id)
    return ok(None, "User deleted", "user_deleted")
