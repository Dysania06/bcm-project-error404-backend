# controllers/documents_tags_controller.py
from models.models import db
from models.document_model import Document
from models.tag_model import Tag

class DocumentsTagsController:
    @staticmethod
    def add_tag_to_document(document_id, tag_id):
        document = Document.query.get(document_id)
        tag = Tag.query.get(tag_id)

        if not document or not tag:
            return {"message": "Document or Tag not found"}, 404

        if tag not in document.tags:
            document.tags.append(tag)
            db.session.commit()

        return {"message": f"Tag {tag.name} added to Document {document.title}"}

    @staticmethod
    def remove_tag_from_document(document_id, tag_id):
        document = Document.query.get(document_id)
        tag = Tag.query.get(tag_id)

        if not document or not tag:
            return {"message": "Document or Tag not found"}, 404

        if tag in document.tags:
            document.tags.remove(tag)
            db.session.commit()

        return {"message": f"Tag {tag.name} removed from Document {document.title}"}

    @staticmethod
    def get_tags_of_document(document_id):
        document = Document.query.get(document_id)
        if not document:
            return {"message": "Document not found"}, 404

        tags = [{"id": tag.id, "name": tag.name} for tag in document.tags]
        return tags

    @staticmethod
    def get_documents_of_tag(tag_id):
        tag = Tag.query.get(tag_id)
        if not tag:
            return {"message": "Tag not found"}, 404

        documents = [{"id": doc.id, "title": doc.title} for doc in tag.documents]
        return documents
