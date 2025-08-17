# File: routes/posts_tags_routes.py
from flask import Blueprint
from controllers.posts_tags_controller import PostsTagsController

posts_tags_bp = Blueprint("posts_tags", __name__, url_prefix="/posts_tags")

# Gán Tag vào Post
@posts_tags_bp.route("/<int:post_id>/tags/<int:tag_id>", methods=["POST"])
def add_tag_to_post(post_id, tag_id):
    return PostsTagsController.add_tag_to_post(post_id, tag_id)

# Xoá Tag khỏi Post
@posts_tags_bp.route("/<int:post_id>/tags/<int:tag_id>", methods=["DELETE"])
def remove_tag_from_post(post_id, tag_id):
    return PostsTagsController.remove_tag_from_post(post_id, tag_id)

# Lấy danh sách Tag của Post
@posts_tags_bp.route("/<int:post_id>/tags", methods=["GET"])
def get_tags_of_post(post_id):
    return PostsTagsController.get_tags_of_post(post_id)

# Lấy danh sách Post theo Tag
@posts_tags_bp.route("/tags/<int:tag_id>/posts", methods=["GET"])
def get_posts_of_tag(tag_id):
    return PostsTagsController.get_posts_of_tag(tag_id)
