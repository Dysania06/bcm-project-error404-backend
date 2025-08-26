import uuid
from models.bookmark_model import Bookmark
from repositories.bookmark_repository import BookmarkRepository
#  Bookmark service class
class BookmarkService:
    @staticmethod
    def get_all_bookmarks():
        return BookmarkRepository.get_all()
#  Get bookmark by id
    @staticmethod
    def get_bookmark(bookmark_id):
        return BookmarkRepository.get_by_id(bookmark_id)
#  Create new bookmark
    @staticmethod
    def create_bookmark(data):
        new_bookmark = Bookmark(
            id=str(uuid.uuid4()),
            user_id=data.get("user_id"),
            post_id=data.get("post_id")
        )
        return BookmarkRepository.create(new_bookmark)
#  Update bookmark
    @staticmethod
    def update_bookmark(bookmark, data):
        bookmark.user_id = data.get("user_id", bookmark.user_id)
        bookmark.post_id = data.get("post_id", bookmark.post_id)
        BookmarkRepository.update()
        return bookmark
#  Delete bookmark
    @staticmethod
    def delete_bookmark(bookmark):
        BookmarkRepository.delete(bookmark)
