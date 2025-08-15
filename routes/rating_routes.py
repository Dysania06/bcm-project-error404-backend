from flask import Blueprint, request, jsonify
from models.rating_model import Rating
from schemas.rating_schema import rating_schema, ratings_schema

rating_bp = Blueprint('rating_bp', __name__)

@rating_bp.route('/ratings', methods=['GET'])
def get_ratings():
    return jsonify(ratings_schema.dump(Rating.get_all()))

@rating_bp.route('/ratings/<string:id>', methods=['GET'])
def get_rating(id):
    rating = Rating.get_by_id(id)
    return jsonify(rating_schema.dump(rating)) if rating else (jsonify({'message': 'Rating not found'}), 404)

@rating_bp.route('/ratings', methods=['POST'])
def create_rating():
    new_rating = Rating(**request.get_json())
    new_rating.save_to_db()
    return jsonify(rating_schema.dump(new_rating)), 201

@rating_bp.route('/ratings/<string:id>', methods=['PUT'])
def update_rating(id):
    rating = Rating.get_by_id(id)
    if not rating:
        return jsonify({'message': 'Rating not found'}), 404
    for k, v in request.get_json().items():
        setattr(rating, k, v)
    rating.save_to_db()
    return jsonify(rating_schema.dump(rating))

@rating_bp.route('/ratings/<string:id>', methods=['DELETE'])
def delete_rating(id):
    rating = Rating.get_by_id(id)
    if not rating:
        return jsonify({'message': 'Rating not found'}), 404
    rating.delete_from_db()
    return jsonify({'message': 'Rating deleted successfully'})
