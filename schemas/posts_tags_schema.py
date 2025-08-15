from . import ma
from models.posts_tags_model import PostsTags

class PostTagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PostsTags
        load_instance = True

post_tag_schema = PostTagSchema()
posts_tags_schema = PostTagSchema(many=True)
