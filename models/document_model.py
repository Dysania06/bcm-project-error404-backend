# File: models/document_model.py
from models.base_model import BaseModel
from models.models import db

class Document(BaseModel):
    __tablename__ = 'documents'
    document_id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.Text)
    uploaded_by = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # Mối quan hệ
    user = db.relationship('User', backref='documents')
    
    def to_json(self):
        return {
            'document_id': self.document_id,
            'title': self.title,
            'content': self.content,
            'uploaded_by': self.uploaded_by
        }