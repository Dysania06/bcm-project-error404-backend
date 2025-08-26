from schemas import ma
from models.post_model import Post
# post schema
class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
# single and multiple post schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
