from schemas import ma
from models.tag_model import Tag
# tag schema
class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        load_instance = True
# single and multiple tag schema
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
