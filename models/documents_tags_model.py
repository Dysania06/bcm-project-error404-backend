from models.models import db

class DocumentTag(db.Model):
    __tablename__ = 'documents_tags'

    document_id = db.Column(db.String(36), db.ForeignKey('documents.id'), primary_key=True)
    tag_id = db.Column(db.String(36), db.ForeignKey('tags.id'), primary_key=True)

    # Quan hệ ngược
    document = db.relationship("Document", back_populates="tags")
    tag = db.relationship("Tag", back_populates="documents")
