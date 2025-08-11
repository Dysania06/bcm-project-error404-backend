# File: models/document_tag_model.py
from models.base_model import BaseModel
from models.models import db

class DocumentsTags(BaseModel):
    __tablename__ = 'documents_tags'
    document_tag_id = db.Column(db.String(50), primary_key=True)
    document_id = db.Column(db.String(50), db.ForeignKey('documents.document_id'))
    tag_id = db.Column(db.String(50), db.ForeignKey('tags.tag_id'))

    document = db.relationship('Document', backref='document_tags')
    tag = db.relationship('Tag', backref='document_tags')

    def to_json(self):
        return {
            'document_tag_id': self.document_tag_id,
            'document_id': self.document_id,
            'tag_id': self.tag_id
        }