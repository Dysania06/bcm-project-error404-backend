from flask import jsonify, request
from services.bookmark_service import BookmarkService
# get all bookmarks
def get_all_bookmarks():
    bookmarks = BookmarkService.get_all_bookmarks()
    return jsonify([bm.to_json() for bm in bookmarks]), 200
# get bookmark by id
def get_bookmark(bookmark_id):
    bookmark = BookmarkService.get_bookmark(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 200
    return jsonify(bookmark.to_json()), 200
# create bookmark 
def create_bookmark():
    data = request.get_json()
    bookmark = BookmarkService.create_bookmark(data)
    return jsonify({"message": "Bookmark created successfully", "bookmark": bookmark.to_json()}), 201
# update bookmark
def update_bookmark(bookmark_id):
    bookmark = BookmarkService.get_bookmark(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 200
    data = request.get_json()
    updated_bookmark = BookmarkService.update_bookmark(bookmark, data)
    return jsonify({"message": "Bookmark updated successfully", "bookmark": updated_bookmark.to_json()}), 200
# delete bookmark
def delete_bookmark(bookmark_id):
    bookmark = BookmarkService.get_bookmark(bookmark_id)
    if not bookmark:
        return jsonify({"message": "Bookmark not found"}), 200
    BookmarkService.delete_bookmark(bookmark)
    return jsonify({"message": "Bookmark deleted successfully"}), 200
