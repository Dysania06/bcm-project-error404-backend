import uuid
from models.models import db

class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    document_id = db.Column(db.String(36), db.ForeignKey("documents.id"), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "document_id": self.document_id
        }
