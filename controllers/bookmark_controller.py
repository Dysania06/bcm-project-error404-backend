from models import Bookmark, db

class BookmarkController:
    @staticmethod
    def get_all():
        return Bookmark.query.all()

    @staticmethod
    def get_by_id(bookmark_id):
        return Bookmark.query.get(bookmark_id)

    @staticmethod
    def create(data):
        new_bookmark = Bookmark(**data)
        db.session.add(new_bookmark)
        db.session.commit()
        return new_bookmark

    @staticmethod
    def update(bookmark, data):
        for key, value in data.items():
            setattr(bookmark, key, value)
        db.session.commit()
        return bookmark

    @staticmethod
    def delete(bookmark):
        db.session.delete(bookmark)
        db.session.commit()
