from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.activity_service import ActivityService
from utils.responses import ok, created, client_error, unauthorized, not_found
from utils.validators import required_fields

activity_bp = Blueprint("activities", __name__, url_prefix="/activities")


@activity_bp.route("", methods=["POST"])
@jwt_required()
def create_activity():
    data = request.get_json() or {}
    missing = required_fields(data, ["title"])
    if missing:
        return client_error("Missing required fields", "missing_fields", errors={"missing": missing})

    user_id = get_jwt_identity()
    activity = ActivityService.create(user_id, data)
    return created(activity.to_dict(), "Activity created", "activity_created")


@activity_bp.route("", methods=["GET"])
@jwt_required()
def list_all():
    activities = ActivityService.get_all()
    return ok([a.to_dict() for a in activities], "Activities listed", "activities_listed")


@activity_bp.route("/me", methods=["GET"])
@jwt_required()
def list_mine():
    user_id = get_jwt_identity()
    activities = ActivityService.get_by_user(user_id)
    return ok([a.to_dict() for a in activities], "User activities listed", "my_activities_listed")


@activity_bp.route("/<int:activity_id>", methods=["PUT"])
@jwt_required()
def update_activity(activity_id):
    data = request.get_json() or {}
    activity = ActivityService.get_by_id(activity_id)

    if not activity:
        return not_found("Activity not found", "activity_not_found")

    user_id = get_jwt_identity()
    if activity.user_id != user_id:
        return unauthorized("You cannot edit another user's activity", "forbidden_action")

    updated = ActivityService.update(activity_id, data)
    return ok(updated.to_dict(), "Activity updated", "activity_updated")


@activity_bp.route("/<int:activity_id>", methods=["DELETE"])
@jwt_required()
def delete_activity(activity_id):
    activity = ActivityService.get_by_id(activity_id)

    if not activity:
        return not_found("Activity not found", "activity_not_found")

    user_id = get_jwt_identity()
    if activity.user_id != user_id:
        return unauthorized("You cannot delete another user's activity", "forbidden_action")

    ActivityService.delete(activity_id)
    return ok(None, "Activity deleted", "activity_deleted")
