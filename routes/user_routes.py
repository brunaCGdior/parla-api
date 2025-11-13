from flask import Blueprint, request
from services.user_service import UserService
from utils.responses import ok, created, error
from flask_jwt_extended import jwt_required

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("", methods=["GET"])
@jwt_required()
def list_users():
    return ok(UserService.list_users())

    @user_bp.route("/<int:user_id>", methods=["GET"])
    @jwt_required()
    def get_user(user_id):
        u = UserService.get_user(user_id)
            if not u:
                    return error("User not found", 404)
                        return ok(u)

                        @user_bp.route("/<int:user_id>", methods=["PUT"])
                        @jwt_required()
                        def update_user(user_id):
                            data = request.get_json()
                                u = UserService.update_user(user_id, data)
                                    return ok(u, "User updated")

                                    @user_bp.route("/<int:user_id>", methods=["DELETE"])
                                    @jwt_required()
                                    def delete_user(user_id):
                                        if UserService.delete_user(user_id):
                                                return ok(msg="Deleted")
                                                    return error("Not found", 404)
                                                    