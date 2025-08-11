# File: models/rating_model.py
from models.base_model import BaseModel
from models.models import db

class Rating(BaseModel):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.String(50), primary_key=True)
    star_rating = db.Column(db.Integer)
    rated_by = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    document_id = db.Column(db.String(50), db.ForeignKey('documents.document_id'))

    def to_json(self):
        return {
            'rating_id': self.rating_id,
            'star_rating': self.star_rating,
            'rated_by': self.rated_by,
            'document_id': self.document_id
        }