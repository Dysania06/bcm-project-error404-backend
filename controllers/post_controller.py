from flask import jsonify, request
from models.post_model import Post, db
import uuid
from datetime import datetime
# get all posts
def get_all_posts():
    posts = Post.query.all()
    return jsonify([post.to_json() for post in posts]), 200
# get post by id
def get_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 200
    return jsonify(post.to_json()), 200
# create post
def create_post():
    data = request.json
    try:
        new_post = Post(
            id=str(uuid.uuid4()),
            title=data.get("title"),
            content=data.get("content"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_post)
        db.session.commit()
        return jsonify({"message": "Post created successfully", "post": new_post.to_json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
# update post
def update_post(post_id):
    data = request.json
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 200
    try:
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        post.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Post updated successfully", "post": post.to_json()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
# delete post
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 200
    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Post deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
