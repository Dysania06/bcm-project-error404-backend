# File: bookmarks_api.py
from flask import Blueprint, request, jsonify
from models.bookmark_model import Bookmark
from models.models import db

bookmarks_bp = Blueprint('bookmarks', __name__)

# Lấy tất cả bookmark
@bookmarks_bp.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    bookmarks = Bookmark.get_all()
    return jsonify([bookmark.to_json() for bookmark in bookmarks])

# Lấy bookmark theo post_id và user_id
@bookmarks_bp.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['GET'])
def get_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    if bookmark:
        return jsonify(bookmark.to_json())
    return jsonify({'message': 'Bookmark not found'}), 404

# Thêm bookmark mới
@bookmarks_bp.route('/bookmarks', methods=['POST'])
def create_bookmark():
    data = request.get_json()
    new_bookmark = Bookmark(
        document_id=data['document_id'],
        user_id=data['user_id']
    )
    new_bookmark.save_to_db()
    return jsonify({'message': 'Bookmark created successfully'}), 201

# Xóa bookmark
@bookmarks_bp.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['DELETE'])
def delete_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    if bookmark:
        bookmark.delete_from_db()
        return jsonify({'message': 'Bookmark deleted successfully'})
    return jsonify({'message': 'Bookmark not found'}), 404