from schemas import ma
from models.document_model import Document
# document schema
class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        load_instance = True
# single and multiple document schema
document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)
