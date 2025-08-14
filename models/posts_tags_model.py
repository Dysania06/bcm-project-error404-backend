# File: models/post_tag_model.py
from models.base_model import BaseModel
from models.models import db

class PostsTags(BaseModel):
    __tablename__ = 'posts_tags'
    post_tag_id = db.Column(db.String(50), primary_key=True)
    post_id = db.Column(db.String(50), db.ForeignKey('posts.post_id'))
    tag_id = db.Column(db.String(50), db.ForeignKey('tags.tag_id'))

    post = db.relationship('Post', backref='post_tags')
    tag = db.relationship('Tag', backref='post_tags')

    def to_json(self):
        return {
            'post_tag_id': self.post_tag_id,
            'post_id': self.post_id,
            'tag_id': self.tag_id
        }