from flask import Blueprint, request, jsonify
from controllers.post_controller import PostController

post_bp = Blueprint("post_bp", __name__, url_prefix="/posts")

@post_bp.route("/", methods=["GET"])
def get_posts():
    posts = PostController.get_all()
    return jsonify([p.to_json() for p in posts]), 200

@post_bp.route("/<post_id>", methods=["GET"])
def get_post(post_id):
    post = PostController.get_by_id(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    return jsonify(post.to_json()), 200

@post_bp.route("/", methods=["POST"])
def create_post():
    data = request.json
    post = PostController.create(data)
    return jsonify(post.to_json()), 201

@post_bp.route("/<post_id>", methods=["PUT"])
def update_post(post_id):
    post = PostController.get_by_id(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    data = request.json
    post = PostController.update(post, data)
    return jsonify(post.to_json()), 200

@post_bp.route("/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = PostController.get_by_id(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    PostController.delete(post)
    return jsonify({"message": "Post deleted"}), 200
