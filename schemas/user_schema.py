from schemas import ma
from models.user_model import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("user_password",)  # Ẩn password khi trả về JSON

user_schema = UserSchema()
users_schema = UserSchema(many=True)
