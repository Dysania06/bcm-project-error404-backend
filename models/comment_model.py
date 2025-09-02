import uuid
from models.models import db
# Comment model
class Comment(db.Model):
    __tablename__ = "comments"
# Columns
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
# Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.String(36), db.ForeignKey("posts.id"), nullable=True)
    document_id = db.Column(db.String(36), db.ForeignKey("documents.id"), nullable=True)
# Convert to JSON
    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "document_id": self.document_id,
        }
