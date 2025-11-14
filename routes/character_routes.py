from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.character_service import CharacterService
from utils.responses import ok, created, client_error, unauthorized, not_found
from utils.validators import required_fields

char_bp = Blueprint("characters", __name__, url_prefix="/characters")


@char_bp.route("", methods=["POST"])
@jwt_required()
def create_character():
    data = request.get_json() or {}
    missing = required_fields(data, ["name"])
    if missing:
        return client_error("Missing required fields", "missing_fields", errors={"missing": missing})

    user_id = get_jwt_identity()
    character = CharacterService.create(user_id, data)
    return created(character.to_dict(), "Character created", "character_created")


@char_bp.route("", methods=["GET"])
@jwt_required()
def list_all():
    characters = CharacterService.get_all()
    return ok([c.to_dict() for c in characters], "Characters listed", "characters_listed")


@char_bp.route("/me", methods=["GET"])
@jwt_required()
def list_mine():
    user_id = get_jwt_identity()
    chars = CharacterService.get_by_user(user_id)
    return ok([c.to_dict() for c in chars], "User characters listed", "my_characters_listed")


@char_bp.route("/<int:char_id>", methods=["PUT"])
@jwt_required()
def update_character(char_id):
    data = request.get_json() or {}
    char = CharacterService.get_by_id(char_id)

    if not char:
        return not_found("Character not found", "character_not_found")

    user_id = get_jwt_identity()
    if char.user_id != user_id:
        return unauthorized("You cannot edit another user's character", "forbidden_action")

    updated = CharacterService.update(char_id, data)
    return ok(updated.to_dict(), "Character updated", "character_updated")


@char_bp.route("/<int:char_id>", methods=["DELETE"])
@jwt_required()
def delete_character(char_id):
    char = CharacterService.get_by_id(char_id)

    if not char:
        return not_found("Character not found", "character_not_found")

    user_id = get_jwt_identity()
    if char.user_id != user_id:
        return unauthorized("You cannot delete another user's character", "forbidden_action")

    CharacterService.delete(char_id)
    return ok(None, "Character deleted", "character_deleted")
