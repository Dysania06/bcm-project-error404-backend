from . import ma
from models.documents_tags_model import DocumentsTags

class DocumentTagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentsTags
        load_instance = True

document_tag_schema = DocumentTagSchema()
documents_tags_schema = DocumentTagSchema(many=True)
