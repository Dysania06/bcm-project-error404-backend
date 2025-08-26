from schemas import ma
from models.comment_model import Comment
# comment schema
class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True
# single and multiple comment schema
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
