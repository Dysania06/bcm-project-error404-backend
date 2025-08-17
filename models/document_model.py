import uuid
from models.models import db

class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    # Khóa ngoại
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    # Quan hệ
    tags = db.relationship("Tag", secondary="documents_tags", backref="documents", lazy="joined")
    comments = db.relationship("Comment", backref="document", lazy=True, cascade="all, delete-orphan")

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "file_path": self.file_path,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id,
        }
