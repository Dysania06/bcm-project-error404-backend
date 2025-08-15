from . import ma
from models.document_model import Document

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        load_instance = True

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)
