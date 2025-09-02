from flask import request, jsonify
from services.bookmark_service import BookmarkService
# get all bookmarks
def get_all_bookmarks():
    bookmarks = BookmarkService.get_all_bookmarks()
    return jsonify(bookmarks), 200
# get bookmark by id
def get_bookmark(bookmark_id):
    bookmark = BookmarkService.get_bookmark_by_id(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 404
    return jsonify(bookmark), 200
# create bookmark
def create_bookmark():
    data = request.get_json()
    new_bookmark, error = BookmarkService.create_bookmark(data)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Bookmark created successfully", "bookmark": new_bookmark}), 201
# update bookmark
def update_bookmark(bookmark_id):
    data = request.get_json()
    updated_bookmark = BookmarkService.update_bookmark(bookmark_id, data)
    if not updated_bookmark:
        return jsonify({"message": "Bookmark not found"}), 404
    return jsonify({"message": "Bookmark updated successfully", "bookmark": updated_bookmark}), 200
# delete bookmark    
def delete_bookmark(bookmark_id):
    deleted = BookmarkService.delete_bookmark(bookmark_id)
    if not deleted:
        return jsonify({"message": "Bookmark not found"}), 404
    return jsonify({"message": "Bookmark deleted successfully"}), 200
