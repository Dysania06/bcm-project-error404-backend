from flask import jsonify, request
from services.comment_service import CommentService
# get all comments
def get_all_comments():
    comments = CommentService.get_all_comments()
    return jsonify([c.to_json() for c in comments]), 200
# get comment by id
def get_comment(comment_id):
    comment = CommentService.get_comment(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 200
    return jsonify(comment.to_json()), 200
# create comment
def create_comment():
    data = request.get_json()
    comment = CommentService.create_comment(data)
    return jsonify({"message": "Comment created successfully", "comment": comment.to_json()}), 201
# update comment
def update_comment(comment_id):
    comment = CommentService.get_comment(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 200
    data = request.get_json()
    updated_comment = CommentService.update_comment(comment, data)
    return jsonify({"message": "Comment updated successfully", "comment": updated_comment.to_json()}), 200
# delete comment
def delete_comment(comment_id):
    comment = CommentService.get_comment(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 200
    CommentService.delete_comment(comment)
    return jsonify({"message": "Comment deleted successfully"}), 200
