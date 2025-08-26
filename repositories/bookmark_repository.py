from models.bookmark_model import Bookmark, db
# repository for Bookmark model
class BookmarkRepository:
    @staticmethod
    def get_all():
        return Bookmark.query.all()
# get bookmark by id
    @staticmethod
    def get_by_id(bookmark_id):
        return Bookmark.query.get(bookmark_id)
# create bookmark
    @staticmethod
    def create(bookmark):
        db.session.add(bookmark)
        db.session.commit()
        return bookmark
# update bookmark
    @staticmethod
    def update():
        db.session.commit()
# delete bookmark
    @staticmethod
    def delete(bookmark):
        db.session.delete(bookmark)
        db.session.commit()
