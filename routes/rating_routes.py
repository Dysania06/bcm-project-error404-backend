from flask import Blueprint
from controllers import rating_controller
# create blueprint for rating
rating_bp = Blueprint("rating_bp", __name__, url_prefix="/ratings")
# call controller from routes
rating_bp.route("/", methods=["GET"])(rating_controller.get_all_ratings)
rating_bp.route("/<rating_id>", methods=["GET"])(rating_controller.get_rating)
rating_bp.route("/", methods=["POST"])(rating_controller.create_rating)
rating_bp.route("/<rating_id>", methods=["PUT"])(rating_controller.update_rating)
rating_bp.route("/<rating_id>", methods=["DELETE"])(rating_controller.delete_rating)
