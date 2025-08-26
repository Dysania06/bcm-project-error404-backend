from flask import Blueprint
from controllers import user_controller
# create blueprint for user
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")
# call controller from routes
user_bp.route("/", methods=["GET"])(user_controller.get_all_users)
user_bp.route("/<user_id>", methods=["GET"])(user_controller.get_user)
user_bp.route("/", methods=["POST"])(user_controller.create_user)
user_bp.route("/<user_id>", methods=["PUT"])(user_controller.update_user)
user_bp.route("/<user_id>", methods=["DELETE"])(user_controller.delete_user)
