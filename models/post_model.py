import uuid
from models.models import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Khóa ngoại
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    # Quan hệ
    comments = db.relationship("Comment", backref="post", lazy=True, cascade="all, delete-orphan")
    ratings = db.relationship("Rating", backref="post", lazy=True, cascade="all, delete-orphan")
    tags = db.relationship("Tag", secondary="posts_tags", backref="posts", lazy="joined")

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id,
        }
