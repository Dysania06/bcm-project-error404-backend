# File: models/bookmark_model.py
from models.base_model import BaseModel
from models.models import db

class Bookmark(BaseModel):
    __tablename__ = 'bookmarks'
    bookmark_id = db.Column(db.String(50), primary_key=True)
    post_id = db.Column(db.String(50), db.ForeignKey('posts.post_id'))
    bookmarked_by = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    
    post = db.relationship('Post', backref='bookmarks')
    user = db.relationship('User', backref='bookmarks')

    def to_json(self):
        return {
            'bookmark_id': self.bookmark_id,
            'post_id': self.post_id,
            'bookmarked_by': self.bookmarked_by
        }