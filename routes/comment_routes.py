from flask import Blueprint, request, jsonify
from controllers.comment_controller import CommentController

comment_bp = Blueprint("comment_bp", __name__, url_prefix="/comments")

@comment_bp.route("/", methods=["GET"])
def get_comments():
    comments = CommentController.get_all()
    return jsonify([c.to_json() for c in comments]), 200

@comment_bp.route("/<comment_id>", methods=["GET"])
def get_comment(comment_id):
    comment = CommentController.get_by_id(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 404
    return jsonify(comment.to_json()), 200

@comment_bp.route("/", methods=["POST"])
def create_comment():
    data = request.json
    comment = CommentController.create(data)
    return jsonify(comment.to_json()), 201

@comment_bp.route("/<comment_id>", methods=["PUT"])
def update_comment(comment_id):
    comment = CommentController.get_by_id(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 404
    data = request.json
    comment = CommentController.update(comment, data)
    return jsonify(comment.to_json()), 200

@comment_bp.route("/<comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = CommentController.get_by_id(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 404
    CommentController.delete(comment)
    return jsonify({"message": "Comment deleted"}), 200
