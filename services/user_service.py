import uuid
from models.user_model import User
from repositories.user_repository import UserRepository
# service for User model
class UserService:
    @staticmethod
    def get_all_users():
        return [u.to_json() for u in UserRepository.get_all()]
#   get user by id
    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        return user.to_json() if user else None
# create a new user
    @staticmethod
    def create_user(data):
        if not data.get("username") or not data.get("email") or not data.get("user_password"):
            return None, "Missing required fields"

        if UserRepository.get_by_username(data.get("username")):
            return None, "Username already exists"

        new_user = User(
            id=str(uuid.uuid4()),
            username=data.get("username"),
            user_password=data.get("user_password"),
            email=data.get("email"),
            phone=data.get("phone"),
            age=data.get("age"),
            department=data.get("department")
        )
        UserRepository.create(new_user)
        return new_user.to_json(), None
#   update an existing user
    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return None

        if "username" in data:
            user.username = data["username"]
        if "email" in data:
            user.email = data["email"]
        if "phone" in data:
            user.phone = data["phone"]
        if "age" in data:
            user.age = data["age"]
        if "department" in data:
            user.department = data["department"]

        UserRepository.update()
        return user.to_json()
#   delete a user
    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return None
        UserRepository.delete(user)
        return True
