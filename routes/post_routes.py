from flask import Blueprint, request, jsonify
from models.post_model import Post
from schemas.post_schema import post_schema, posts_schema

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.get_all()
    return jsonify(posts_schema.dump(posts))

@post_bp.route('/posts/<string:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        return jsonify(post_schema.dump(post))
    return jsonify({'message': 'Post not found'}), 404

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(**data)
    new_post.save_to_db()
    return jsonify(post_schema.dump(new_post)), 201

@post_bp.route('/posts/<string:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        data = request.get_json()
        for key, value in data.items():
            setattr(post, key, value)
        post.save_to_db()
        return jsonify(post_schema.dump(post))
    return jsonify({'message': 'Post not found'}), 404

@post_bp.route('/posts/<string:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        post.delete_from_db()
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'message': 'Post not found'}), 404
