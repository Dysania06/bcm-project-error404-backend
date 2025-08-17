from flask import Blueprint, request, jsonify
from controllers.bookmark_controller import BookmarkController

bookmark_bp = Blueprint("bookmark_bp", __name__, url_prefix="/bookmarks")

@bookmark_bp.route("/", methods=["GET"])
def get_bookmarks():
    bookmarks = BookmarkController.get_all()
    return jsonify([b.to_json() for b in bookmarks]), 200

@bookmark_bp.route("/<bookmark_id>", methods=["GET"])
def get_bookmark(bookmark_id):
    bookmark = BookmarkController.get_by_id(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 404
    return jsonify(bookmark.to_json()), 200

@bookmark_bp.route("/", methods=["POST"])
def create_bookmark():
    data = request.json
    bookmark = BookmarkController.create(data)
    return jsonify(bookmark.to_json()), 201

@bookmark_bp.route("/<bookmark_id>", methods=["PUT"])
def update_bookmark(bookmark_id):
    bookmark = BookmarkController.get_by_id(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 404
    data = request.json
    bookmark = BookmarkController.update(bookmark, data)
    return jsonify(bookmark.to_json()), 200

@bookmark_bp.route("/<bookmark_id>", methods=["DELETE"])
def delete_bookmark(bookmark_id):
    bookmark = BookmarkController.get_by_id(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 404
    BookmarkController.delete(bookmark)
    return jsonify({"message": "Bookmark deleted"}), 200
