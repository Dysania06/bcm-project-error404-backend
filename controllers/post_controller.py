from flask import request, jsonify
from services.post_service import PostService
# get all posts
def get_all_posts():
    posts = PostService.get_all_posts()
    return jsonify(posts), 200
# get post by id
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    return jsonify(post), 200
# create post
def create_post():
    data = request.get_json()
    new_post, error = PostService.create_post(data)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Post created successfully", "post": new_post}), 201
# update post
def update_post(post_id):
    data = request.get_json()
    updated_post = PostService.update_post(post_id, data)
    if not updated_post:
        return jsonify({"message": "Post not found"}), 404
    return jsonify({"message": "Post updated successfully", "post": updated_post}), 200
# delete post
def delete_post(post_id):
    deleted = PostService.delete_post(post_id)
    if not deleted:
        return jsonify({"message": "Post not found"}), 404
    return jsonify({"message": "Post deleted successfully"}), 200
