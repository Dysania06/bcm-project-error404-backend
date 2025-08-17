from models.models import db

class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.String(36), db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.String(36), db.ForeignKey('tags.id'), primary_key=True)

    # Quan hệ ngược
    post = db.relationship("Post", back_populates="tags")
    tag = db.relationship("Tag", back_populates="posts")
