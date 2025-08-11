# File: models/post_model.py
from models.base_model import BaseModel
from models.models import db

class Post(BaseModel):
    __tablename__ = 'posts'
    post_id = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    posted_by = db.Column(db.String(50), db.ForeignKey('users.user_id'))

    def to_json(self):
        return {
            'post_id': self.post_id,
            'title': self.title,
            'content': self.content,
            'posted_by': self.posted_by
        }