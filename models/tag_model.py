# File: models/tag_model.py
from models.base_model import BaseModel
from models.models import db

class Tag(BaseModel):
    __tablename__ = 'tags'
    tag_id = db.Column(db.String(50), primary_key=True)
    nameposts_tags = db.Column(db.String(100), unique=True, nullable=False)

    def to_json(self):
        return {
            'tag_id': self.tag_id,
            'nameposts_tags': self.tag_name
        }