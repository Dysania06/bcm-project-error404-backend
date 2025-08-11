# File: models/user_model.py
from models.base_model import BaseModel
from models.models import db

class User(BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True) # Tên cột khóa chính là 'id'
    username = db.Column(db.String(50), unique=True, nullable=False) # Độ dài 50
    user_password = db.Column(db.String(225), nullable=False) # Tên cột là 'user_password'
    email = db.Column(db.String(50), unique=True, nullable=False) # Độ dài 50
    phone = db.Column(db.String(50))
    age = db.Column(db.Integer)
    department = db.Column(db.String(50))
    
    # Chúng ta bỏ các cột created_at, updated_at vì lược đồ SQL không có
    
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'age': self.age,
            'department': self.department
        }