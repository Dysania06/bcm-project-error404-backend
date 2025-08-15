from flask import Blueprint, request, jsonify
from models.bookmark_model import Bookmark
from schemas.bookmark_schema import bookmark_schema, bookmarks_schema

bookmark_bp = Blueprint('bookmark_bp', __name__)

@bookmark_bp.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    return jsonify(bookmarks_schema.dump(Bookmark.get_all()))

@bookmark_bp.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['GET'])
def get_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    return jsonify(bookmark_schema.dump(bookmark)) if bookmark else (jsonify({'message': 'Bookmark not found'}), 404)

@bookmark_bp.route('/bookmarks', methods=['POST'])
def create_bookmark():
    new_bookmark = Bookmark(**request.get_json())
    new_bookmark.save_to_db()
    return jsonify(bookmark_schema.dump(new_bookmark)), 201

@bookmark_bp.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['DELETE'])
def delete_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    if not bookmark:
        return jsonify({'message': 'Bookmark not found'}), 404
    bookmark.delete_from_db()
    return jsonify({'message': 'Bookmark deleted successfully'})
