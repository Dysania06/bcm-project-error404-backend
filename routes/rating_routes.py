from flask import Blueprint, request, jsonify
from controllers.rating_controller import RatingController

rating_bp = Blueprint("rating_bp", __name__, url_prefix="/ratings")

@rating_bp.route("/", methods=["GET"])
def get_ratings():
    ratings = RatingController.get_all()
    return jsonify([r.to_json() for r in ratings]), 200

@rating_bp.route("/<rating_id>", methods=["GET"])
def get_rating(rating_id):
    rating = RatingController.get_by_id(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    return jsonify(rating.to_json()), 200

@rating_bp.route("/", methods=["POST"])
def create_rating():
    data = request.json
    rating = RatingController.create(data)
    return jsonify(rating.to_json()), 201

@rating_bp.route("/<rating_id>", methods=["PUT"])
def update_rating(rating_id):
    rating = RatingController.get_by_id(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    data = request.json
    rating = RatingController.update(rating, data)
    return jsonify(rating.to_json()), 200

@rating_bp.route("/<rating_id>", methods=["DELETE"])
def delete_rating(rating_id):
    rating = RatingController.get_by_id(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    RatingController.delete(rating)
    return jsonify({"message": "Rating deleted"}), 200
