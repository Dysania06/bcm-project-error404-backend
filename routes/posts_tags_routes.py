from flask import Blueprint
from controllers import posts_tags_controller
# create blueprint for posts_tags
posts_tags_bp = Blueprint("posts_tags_bp", __name__, url_prefix="/posts_tags")
# call controller from routes
posts_tags_bp.route("/", methods=["GET"])(posts_tags_controller.get_all_posts_tags)
posts_tags_bp.route("/<record_id>", methods=["GET"])(posts_tags_controller.get_posts_tag)
posts_tags_bp.route("/", methods=["POST"])(posts_tags_controller.create_posts_tags)
posts_tags_bp.route("/<record_id>", methods=["PUT"])(posts_tags_controller.update_posts_tags)
posts_tags_bp.route("/<record_id>", methods=["DELETE"])(posts_tags_controller.delete_posts_tags)
