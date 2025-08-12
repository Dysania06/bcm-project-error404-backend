# File: posts_tags_api.py
from flask import Blueprint, request, jsonify
from models.post_tag_model import PostsTags
from models.models import db

posts_tags_bp = Blueprint('posts_tags', __name__)

# Lấy tất cả post_tag
@posts_tags_bp.route('/posts_tags', methods=['GET'])
def get_posts_tags():
    posts_tags = PostsTags.get_all()
    return jsonify([post_tag.to_json() for post_tag in posts_tags])

# Lấy post_tag theo post_id và tag_id
@posts_tags_bp.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['GET'])
def get_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    if post_tag:
        return jsonify(post_tag.to_json())
    return jsonify({'message': 'Post Tag not found'}), 404

# Thêm post_tag mới
@posts_tags_bp.route('/posts_tags', methods=['POST'])
def create_post_tag():
    data = request.get_json()
    new_post_tag = PostsTags(
        post_id=data['post_id'],
        tag_id=data['tag_id']
    )
    new_post_tag.save_to_db()
    return jsonify({'message': 'Post Tag created successfully'}), 201

# Xóa post_tag
@posts_tags_bp.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['DELETE'])
def delete_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    if post_tag:
        post_tag.delete_from_db()
        return jsonify({'message': 'Post Tag deleted successfully'})
    return jsonify({'message': 'Post Tag not found'}), 404