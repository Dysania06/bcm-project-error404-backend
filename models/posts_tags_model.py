from models.models import db

posts_tags = db.Table(
    "posts_tags",
    db.Column("post_id", db.String(36), db.ForeignKey("posts.id"), primary_key=True),
    db.Column("tag_id", db.String(36), db.ForeignKey("tags.id"), primary_key=True)
)
