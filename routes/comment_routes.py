from flask import Blueprint
from controllers import comment_controller
# create blueprint for comment
comment_bp = Blueprint("comment_bp", __name__, url_prefix="/comments")
# call controller from routes
comment_bp.route("/", methods=["GET"])(comment_controller.get_all_comments)
comment_bp.route("/<comment_id>", methods=["GET"])(comment_controller.get_comment)
comment_bp.route("/", methods=["POST"])(comment_controller.create_comment)
comment_bp.route("/<comment_id>", methods=["PUT"])(comment_controller.update_comment)
comment_bp.route("/<comment_id>", methods=["DELETE"])(comment_controller.delete_comment)
