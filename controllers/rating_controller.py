from flask import jsonify, request
from services.rating_service import RatingService
# get all ratings
def get_all_ratings():
    ratings = RatingService.get_all_ratings()
    return jsonify([rating.to_json() for rating in ratings]), 200
# get rating by id
def get_rating(rating_id):
    rating = RatingService.get_rating(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    return jsonify(rating.to_json()), 200
# create rating
def create_rating():
    data = request.get_json()
    rating = RatingService.create_rating(data)
    return jsonify({"message": "Rating created successfully", "rating": rating.to_json()}), 201
# update rating
def update_rating(rating_id):
    rating = RatingService.get_rating(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    data = request.get_json()
    updated_rating = RatingService.update_rating(rating, data)
    return jsonify({"message": "Rating updated successfully", "rating": updated_rating.to_json()}), 200
# delete rating
def delete_rating(rating_id):
    rating = RatingService.get_rating(rating_id)
    if not rating:
        return jsonify({"message": "Rating not found"}), 404
    RatingService.delete_rating(rating)
    return jsonify({"message": "Rating deleted successfully"}), 200
