import uuid
from models.models import db

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }
