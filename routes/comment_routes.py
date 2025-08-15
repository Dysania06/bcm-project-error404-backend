from flask import Blueprint, request, jsonify
from models.comment_model import Comment
from schemas.comment_schema import comment_schema, comments_schema

comment_bp = Blueprint('comment_bp', __name__)

@comment_bp.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments_schema.dump(Comment.get_all()))

@comment_bp.route('/comments/<string:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.get_by_id(id)
    return jsonify(comment_schema.dump(comment)) if comment else (jsonify({'message': 'Comment not found'}), 404)

@comment_bp.route('/comments', methods=['POST'])
def create_comment():
    new_comment = Comment(**request.get_json())
    new_comment.save_to_db()
    return jsonify(comment_schema.dump(new_comment)), 201

@comment_bp.route('/comments/<string:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.get_by_id(id)
    if not comment:
        return jsonify({'message': 'Comment not found'}), 404
    for k, v in request.get_json().items():
        setattr(comment, k, v)
    comment.save_to_db()
    return jsonify(comment_schema.dump(comment))

@comment_bp.route('/comments/<string:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.get_by_id(id)
    if not comment:
        return jsonify({'message': 'Comment not found'}), 404
    comment.delete_from_db()
    return jsonify({'message': 'Comment deleted successfully'})
