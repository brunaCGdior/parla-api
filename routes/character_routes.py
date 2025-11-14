from flask import Blueprint, request
from services.character_service import CharacterService
from utils.responses import ok, created, error
from flask_jwt_extended import jwt_required, get_jwt_identity

char_bp = Blueprint("characters", __name__, url_prefix="/characters")

@char_bp.route("", methods=["POST"])
@jwt_required()
def create_character():
    uid = get_jwt_identity()
    data = request.get_json()
    c = CharacterService.create_character(uid, data["name"], data.get("avatar"))
    return created(c)

@char_bp.route("", methods=["GET"])
@jwt_required()
def list_characters():
    return ok(CharacterService.list_characters())

@char_bp.route("/me", methods=["GET"])
@jwt_required()
def my_characters():
    uid = get_jwt_identity()
    return ok(CharacterService.list_by_user(uid))

@char_bp.route("/<int:cid>", methods=["GET"])
@jwt_required()
def get_character(cid):
    c = CharacterService.get_character(cid)
    if not c:
        return error("Not found", 404)
    return ok(c)

@char_bp.route("/<int:cid>", methods=["PUT"])
@jwt_required()
def update_character(cid):
    data = request.get_json()
    c = CharacterService.update_character(cid, data)
    return ok(c, "Updated")

@char_bp.route("/<int:cid>", methods=["DELETE"])
@jwt_required()
def delete_character(cid):
    if CharacterService.delete_character(cid):
        return ok(msg="Deleted")
    return error("Not found", 404)
