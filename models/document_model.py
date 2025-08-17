import uuid
from models.models import db
from models.documents_tags_model import DocumentTag

class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=True)
    upload_date = db.Column(db.DateTime, server_default=db.func.now()) # Ngày tải lên
    update_date = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

     # Quan hệ nhiều-nhiều với Tag
    tags = db.relationship("DocumentTag", back_populates="document", cascade="all, delete-orphan")

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
            "upload_date": self.upload_date,
            "update_date": self.update_date,
            "user_id": self.user_id,
        }
