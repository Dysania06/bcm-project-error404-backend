import uuid
from models.user_model import User
from repositories.user_repository import UserRepository
# User service class
class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()
# Get user by id
    @staticmethod
    def get_user(user_id):
        return UserRepository.get_by_id(user_id)
# Get user by email
    @staticmethod
    def create_user(data):
        new_user = User(
            id=str(uuid.uuid4()),
            username=data.get("username"),
            user_password=data.get("user_password"),
            email=data.get("email"),
            phone=data.get("phone"),
            age=data.get("age"),
            department=data.get("department")
        )
        return UserRepository.create(new_user)
# Update user
    @staticmethod
    def update_user(user, data):
        user.username = data.get("username", user.username)
        user.user_password = data.get("user_password", user.user_password)
        user.email = data.get("email", user.email)
        user.phone = data.get("phone", user.phone)
        user.age = data.get("age", user.age)
        user.department = data.get("department", user.department)
        UserRepository.update()
        return user
# Delete user
    @staticmethod
    def delete_user(user):
        UserRepository.delete(user)
