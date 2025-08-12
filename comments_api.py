# File: comments_api.py
from flask import Blueprint, request, jsonify
from models.comment_model import Comment
from models.models import db

comments_bp = Blueprint('comments', __name__)

# Lấy tất cả comment
@comments_bp.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.get_all()
    return jsonify([comment.json() for comment in comments])

# Lấy comment theo id
@comments_bp.route('/comments/<string:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        return jsonify(comment.json())
    return jsonify({'message': 'Comment not found'}), 404

# Thêm comment mới
@comments_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    new_comment = Comment(
        comment_id=data['comment_id'],
        content=data['content'],
        commented_by=data['commented_by'],
        post_id=data.get('post_id'),
        document_id=data.get('document_id')
    )
    new_comment.save_to_db()
    return jsonify({'message': 'Comment created successfully'}), 201

# Cập nhật comment
@comments_bp.route('/comments/<string:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        data = request.get_json()
        comment.content = data.get('content', comment.content)
        comment.commented_by = data.get('commented_by', comment.commented_by)
        comment.post_id = data.get('post_id', comment.post_id)
        comment.document_id = data.get('document_id', comment.document_id)
        comment.save_to_db()
        return jsonify({'message': 'Comment updated successfully'})
    return jsonify({'message': 'Comment not found'}), 404

# Xóa comment
@comments_bp.route('/comments/<string:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        comment.delete_from_db()
        return jsonify({'message': 'Comment deleted successfully'})
    return jsonify({'message': 'Comment not found'}), 404