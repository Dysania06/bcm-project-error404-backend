import uuid
from datetime import datetime
from models.bookmark_model import Bookmark
from repositories.bookmark_repository import BookmarkRepository
# service for Bookmark model
class BookmarkService:
    @staticmethod
    def get_all_bookmarks():
        return [b.to_json() for b in BookmarkRepository.get_all()]
#   get bookmark by id
    @staticmethod
    def get_bookmark_by_id(bookmark_id):
        bookmark = BookmarkRepository.get_by_id(bookmark_id)
        return bookmark.to_json() if bookmark else None
# create a new bookmark
    @staticmethod
    def create_bookmark(data):
        if not data.get("user_id") or not data.get("document_id"):
            return None, "Missing required fields"
# check for duplicate bookmark
        new_bookmark = Bookmark(
            id=str(uuid.uuid4()),
            user_id=data.get("user_id"),
            document_id=data.get("document_id"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        BookmarkRepository.create(new_bookmark)
        return new_bookmark.to_json(), None
# update an existing bookmark
    @staticmethod
    def update_bookmark(bookmark_id, data):
        bookmark = BookmarkRepository.get_by_id(bookmark_id)
        if not bookmark:
            return None

        if "document_id" in data:
            bookmark.document_id = data["document_id"]
        bookmark.updated_at = datetime.utcnow()

        BookmarkRepository.update()
        return bookmark.to_json()
# delete a bookmark
    @staticmethod
    def delete_bookmark(bookmark_id):
        bookmark = BookmarkRepository.get_by_id(bookmark_id)
        if not bookmark:
            return None
        BookmarkRepository.delete(bookmark)
        return True
