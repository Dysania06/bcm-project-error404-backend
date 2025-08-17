import uuid
from models.models import db

class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    score = db.Column(db.Integer, nullable=False)

    # Khóa ngoại
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    document_id = db.Column(db.String(36), db.ForeignKey("documents.id"), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "score": self.score,
            "user_id": self.user_id,
            "document_id": self.document_id
        }
