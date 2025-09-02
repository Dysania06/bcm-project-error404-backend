import uuid
from models.models import db
from models.posts_tags_model import posts_tags
from models.documents_tags_model import documents_tags

# Tag model
class Tag(db.Model):
    __tablename__ = "tags"
# Columns
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tag_name = db.Column(db.String(50), nullable=False, unique=True)

     # relationships many-to-many with Post and Document through association tables
    posts = db.relationship("PostTag", back_populates="tag", cascade="all, delete-orphan")
    documents = db.relationship("DocumentTag", back_populates="tag", cascade="all, delete-orphan")
    # converts to JSON
    def to_json(self):
        return {
            "id": self.id,
            "tag_name": self.tag_name,
        }
