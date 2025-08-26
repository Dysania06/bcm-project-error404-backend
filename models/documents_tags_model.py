from models.models import db

documents_tags = db.Table(
    "documents_tags",
    db.Column("document_id", db.String(36), db.ForeignKey("documents.id"), primary_key=True),
    db.Column("tag_id", db.String(36), db.ForeignKey("tags.id"), primary_key=True)
)
