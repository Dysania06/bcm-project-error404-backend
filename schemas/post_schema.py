from . import ma
from models.post_model import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
