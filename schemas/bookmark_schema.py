from . import ma
from models.bookmark_model import Bookmark

class BookmarkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bookmark
        load_instance = True

# Schema cho 1 object
bookmark_schema = BookmarkSchema()

# Schema cho list object
bookmarks_schema = BookmarkSchema(many=True)
