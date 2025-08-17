from schemas import ma
from models.bookmark_model import Bookmark

class BookmarkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bookmark
        load_instance = True

bookmark_schema = BookmarkSchema()
bookmarks_schema = BookmarkSchema(many=True)
