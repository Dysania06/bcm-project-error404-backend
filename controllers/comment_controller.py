from flask import request, jsonify
from services.comment_service import CommentService
# get all comments
def get_all_comments():
    comments = CommentService.get_all_comments()
    return jsonify(comments), 200
# get comment by id
def get_comment(comment_id):
    comment = CommentService.get_comment_by_id(comment_id)
    if not comment:
        return jsonify({"message": "Comment not found"}), 404
    return jsonify(comment), 200
# create comment
def create_comment():
    data = request.get_json()
    new_comment, error = CommentService.create_comment(data)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Comment created successfully", "comment": new_comment}), 201
# update comment
def update_comment(comment_id):
    data = request.get_json()
    updated_comment = CommentService.update_comment(comment_id, data)
    if not updated_comment:
        return jsonify({"message": "Comment not found"}), 404
    return jsonify({"message": "Comment updated successfully", "comment": updated_comment}), 200
# delete comment
def delete_comment(comment_id):
    deleted = CommentService.delete_comment(comment_id)
    if not deleted:
        return jsonify({"message": "Comment not found"}), 404
    return jsonify({"message": "Comment deleted successfully"}), 200
