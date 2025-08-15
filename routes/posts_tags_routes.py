from flask import Blueprint, request, jsonify
from models.posts_tags_model import PostsTags
from schemas.posts_tags_schema import post_tag_schema, posts_tags_schema

posts_tags_bp = Blueprint('posts_tags_bp', __name__)

@posts_tags_bp.route('/posts_tags', methods=['GET'])
def get_posts_tags():
    return jsonify(posts_tags_schema.dump(PostsTags.get_all()))

@posts_tags_bp.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['GET'])
def get_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    return jsonify(post_tag_schema.dump(post_tag)) if post_tag else (jsonify({'message': 'Post Tag not found'}), 404)

@posts_tags_bp.route('/posts_tags', methods=['POST'])
def create_post_tag():
    new_post_tag = PostsTags(**request.get_json())
    new_post_tag.save_to_db()
    return jsonify(post_tag_schema.dump(new_post_tag)), 201

@posts_tags_bp.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['DELETE'])
def delete_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    if not post_tag:
        return jsonify({'message': 'Post Tag not found'}), 404
    post_tag.delete_from_db()
    return jsonify({'message': 'Post Tag deleted successfully'})
