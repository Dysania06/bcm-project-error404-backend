from schemas import ma
from models.bookmark_model import Bookmark
# bookmark schema
class BookmarkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bookmark
        load_instance = True
# single and multiple bookmark schema
bookmark_schema = BookmarkSchema()
bookmarks_schema = BookmarkSchema(many=True)
