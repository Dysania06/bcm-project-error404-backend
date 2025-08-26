from flask import Blueprint
from controllers import bookmark_controller
# create blueprint for bookmark
bookmark_bp = Blueprint("bookmark_bp", __name__, url_prefix="/bookmarks")
# call controller from routes 
bookmark_bp.route("/", methods=["GET"])(bookmark_controller.get_all_bookmarks)
bookmark_bp.route("/<bookmark_id>", methods=["GET"])(bookmark_controller.get_bookmark)
bookmark_bp.route("/", methods=["POST"])(bookmark_controller.create_bookmark)
bookmark_bp.route("/<bookmark_id>", methods=["PUT"])(bookmark_controller.update_bookmark)
bookmark_bp.route("/<bookmark_id>", methods=["DELETE"])(bookmark_controller.delete_bookmark)
