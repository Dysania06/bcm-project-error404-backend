import uuid
from datetime import datetime
from models.document_model import Document
from repositories.document_repository import DocumentRepository
# Document service class
class DocumentService:
    @staticmethod
    def get_all_documents():
        return DocumentRepository.get_all()
# Get document by id
    @staticmethod
    def get_document(document_id):
        return DocumentRepository.get_by_id(document_id)
# Create new document
    @staticmethod
    def create_document(data):
        new_document = Document(
            id=str(uuid.uuid4()),
            title=data.get("title"),
            content=data.get("content"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return DocumentRepository.create(new_document)
# Update document
    @staticmethod
    def update_document(document, data):
        document.title = data.get("title", document.title)
        document.content = data.get("content", document.content)
        document.updated_at = datetime.utcnow()
        DocumentRepository.update()
        return document
# Delete document
    @staticmethod
    def delete_document(document):
        DocumentRepository.delete(document)
