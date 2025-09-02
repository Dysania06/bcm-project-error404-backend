import uuid
from datetime import datetime
from models.document_model import Document
from repositories.document_repository import DocumentRepository

class DocumentService:
    @staticmethod
    def get_all_documents():
        return [doc.to_json() for doc in DocumentRepository.get_all()]

    @staticmethod
    def get_document_by_id(document_id):
        doc = DocumentRepository.get_by_id(document_id)
        return doc.to_json() if doc else None

    @staticmethod
    def create_document(data):
        # Validate input
        if not data.get("title") or not data.get("content") or not data.get("created_by"):
            return None, "Missing required fields"
# check for duplicate document
        new_doc = Document(
            id=str(uuid.uuid4()),
            title=data.get("title"),
            content=data.get("content"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        DocumentRepository.create(new_doc)
        return new_doc.to_json(), None
# update an existing document
    @staticmethod
    def update_document(document_id, data):
        doc = DocumentRepository.get_by_id(document_id)
        if not doc:
            return None
# only title and content can be updated
        if "title" in data:
            doc.title = data["title"]
        if "content" in data:
            doc.content = data["content"]

        doc.updated_at = datetime.utcnow()
        DocumentRepository.update()
        return doc.to_json()
# delete a document
    @staticmethod
    def delete_document(document_id):
        doc = DocumentRepository.get_by_id(document_id)
        if not doc:
            return None
        DocumentRepository.delete(doc)
        return True
