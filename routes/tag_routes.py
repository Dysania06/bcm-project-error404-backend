from flask import Blueprint
from controllers import tag_controller

tag_bp = Blueprint("tag_bp", __name__, url_prefix="/tags")

tag_bp.route("/", methods=["GET"])(tag_controller.get_all_tags)
tag_bp.route("/<tag_id>", methods=["GET"])(tag_controller.get_tag)
tag_bp.route("/", methods=["POST"])(tag_controller.create_tag)
tag_bp.route("/<tag_id>", methods=["PUT"])(tag_controller.update_tag)
tag_bp.route("/<tag_id>", methods=["DELETE"])(tag_controller.delete_tag)
