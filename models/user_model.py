import uuid
from models.models import db
# model User
class User(db.Model):
    __tablename__ = "users"
   # columns 
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    department = db.Column(db.String(50), nullable=True)

    # relationships
    posts = db.relationship("Post", backref="user", lazy=True, cascade="all, delete-orphan")
    documents = db.relationship("Document", backref="user", lazy=True, cascade="all, delete-orphan")
    comments = db.relationship("Comment", backref="user", lazy=True, cascade="all, delete-orphan")
    ratings = db.relationship("Rating", backref="user", lazy=True, cascade="all, delete-orphan")
    bookmarks = db.relationship("Bookmark", backref="user", lazy=True, cascade="all, delete-orphan")
# method to convert user object to json
    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "age": self.age,
            "department": self.department,
        }
