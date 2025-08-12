# File: ratings_api.py
from flask import Blueprint, request, jsonify
from models.rating_model import Rating
from models.models import db

ratings_bp = Blueprint('ratings', __name__)

# Lấy tất cả rating
@ratings_bp.route('/ratings', methods=['GET'])
def get_ratings():
    ratings = Rating.get_all()
    return jsonify([rating.to_json() for rating in ratings])

# Lấy rating theo id
@ratings_bp.route('/ratings/<string:rating_id>', methods=['GET'])
def get_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        return jsonify(rating.to_json())
    return jsonify({'message': 'Rating not found'}), 404

# Thêm rating mới
@ratings_bp.route('/ratings', methods=['POST'])
def create_rating():
    data = request.get_json()
    new_rating = Rating(
        rating_id=data['rating_id'],
        star_rating=data['star_rating'],
        rated_by=data['rated_by'],
        document_id=data['document_id']
    )
    new_rating.save_to_db()
    return jsonify({'message': 'Rating created successfully'}), 201

# Cập nhật rating
@ratings_bp.route('/ratings/<string:rating_id>', methods=['PUT'])
def update_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        data = request.get_json()
        rating.star_rating = data.get('star_rating', rating.star_rating)
        rating.rated_by = data.get('rated_by', rating.rated_by)
        rating.document_id = data.get('document_id', rating.document_id)
        rating.save_to_db()
        return jsonify({'message': 'Rating updated successfully'})
    return jsonify({'message': 'Rating not found'}), 404

# Xóa rating
@ratings_bp.route('/ratings/<string:rating_id>', methods=['DELETE'])
def delete_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        rating.delete_from_db()
        return jsonify({'message': 'Rating deleted successfully'})
    return jsonify({'message': 'Rating not found'}), 404