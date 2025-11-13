from flask import Blueprint, request
from services.activity_service import ActivityService
from utils.responses import ok, created, error
from flask_jwt_extended import jwt_required, get_jwt_identity

activity_bp = Blueprint("activities", __name__, url_prefix="/activities")

@activity_bp.route("", methods=["POST"])
@jwt_required()
def create_activity():
    uid = get_jwt_identity()
        data = request.get_json()
            a = ActivityService.create_activity(uid, data["title"], data.get("description"))
                return created(a)

                @activity_bp.route("", methods=["GET"])
                @jwt_required()
                def list_activities():
                    return ok(ActivityService.list_activities())

                    @activity_bp.route("/me", methods=["GET"])
                    @jwt_required()
                    def my_activities():
                        uid = get_jwt_identity()
                            return ok(ActivityService.list_by_user(uid))

                            @activity_bp.route("/<int:aid>", methods=["GET"])
                            @jwt_required()
                            def get_activity(aid):
                                a = ActivityService.get_activity(aid)
                                    if not a:
                                            return error("Not found", 404)
                                                return ok(a)

                                                @activity_bp.route("/<int:aid>", methods=["PUT"])
                                                @jwt_required()
                                                def update_activity(aid):
                                                    data = request.get_json()
                                                        a = ActivityService.update_activity(aid, data)
                                                            return ok(a, "Updated")

                                                            @activity_bp.route("/<int:aid>", methods=["DELETE"])
                                                            @jwt_required()
                                                            def delete_activity(aid):
                                                                if ActivityService.delete_activity(aid):
                                                                        return ok(msg="Deleted")
                                                                            return error("Not found", 404)
                                                                            