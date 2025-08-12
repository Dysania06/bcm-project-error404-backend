# File: posts_api.py
from flask import Blueprint, request, jsonify
from models.post_model import Post
from models.models import db

posts_bp = Blueprint('posts', __name__)

# Lấy tất cả post
@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.get_all()
    return jsonify([post.to_json() for post in posts])

# Lấy post theo id
@posts_bp.route('/posts/<string:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        return jsonify(post.to_json())
    return jsonify({'message': 'Post not found'}), 404

# Thêm post mới
@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(
        post_id=data['post_id'],
        title=data['title'],
        content=data['content'],
        posted_by=data['posted_by']
    )
    new_post.save_to_db()
    return jsonify({'message': 'Post created successfully'}), 201

# Cập nhật post
@posts_bp.route('/posts/<string:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.posted_by = data.get('posted_by', post.posted_by)
        post.save_to_db()
        return jsonify({'message': 'Post updated successfully'})
    return jsonify({'message': 'Post not found'}), 404

# Xóa post
@posts_bp.route('/posts/<string:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        post.delete_from_db()
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'message': 'Post not found'}), 404