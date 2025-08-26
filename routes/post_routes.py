from flask import Blueprint
from controllers import post_controller
# create blueprint for post
post_bp = Blueprint("post_bp", __name__, url_prefix="/posts")
# call controller from routes
post_bp.route("/", methods=["GET"])(post_controller.get_all_posts)
post_bp.route("/<post_id>", methods=["GET"])(post_controller.get_post)
post_bp.route("/", methods=["POST"])(post_controller.create_post)
post_bp.route("/<post_id>", methods=["PUT"])(post_controller.update_post)
post_bp.route("/<post_id>", methods=["DELETE"])(post_controller.delete_post)
