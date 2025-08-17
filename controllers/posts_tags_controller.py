# File: controllers/posts_tags_controller.py
from flask import jsonify, request
from models.models import db
from models.post_model import Post
from models.tag_model import Tag

class PostsTagsController:
    @staticmethod
    def add_tag_to_post(post_id, tag_id):
        post = Post.query.get(post_id)
        tag = Tag.query.get(tag_id)

        if not post or not tag:
            return jsonify({"message": "Post or Tag not found"}), 404

        if tag in post.tags:
            return jsonify({"message": "Tag already added to post"}), 400

        post.tags.append(tag)
        db.session.commit()
        return jsonify({"message": f"Tag {tag_id} added to Post {post_id}"}), 201

    @staticmethod
    def remove_tag_from_post(post_id, tag_id):
        post = Post.query.get(post_id)
        tag = Tag.query.get(tag_id)

        if not post or not tag:
            return jsonify({"message": "Post or Tag not found"}), 404

        if tag not in post.tags:
            return jsonify({"message": "Tag not found in post"}), 400

        post.tags.remove(tag)
        db.session.commit()
        return jsonify({"message": f"Tag {tag_id} removed from Post {post_id}"}), 200

    @staticmethod
    def get_tags_of_post(post_id):
        post = Post.query.get(post_id)
        if not post:
            return jsonify({"message": "Post not found"}), 404

        tags = [{"id": tag.id, "name": tag.name} for tag in post.tags]
        return jsonify(tags), 200

    @staticmethod
    def get_posts_of_tag(tag_id):
        tag = Tag.query.get(tag_id)
        if not tag:
            return jsonify({"message": "Tag not found"}), 404

        posts = [{"id": post.id, "title": post.title} for post in tag.posts]
        return jsonify(posts), 200
