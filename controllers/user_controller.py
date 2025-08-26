from flask import jsonify, request
from services.user_service import UserService
# get all users
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([u.to_json() for u in users]), 200
# get user by id
def get_user(user_id):
    user = UserService.get_user(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 200
    return jsonify(user.to_json()), 200
# create user
def create_user():
    data = request.get_json()
    user = UserService.create_user(data)
    return jsonify({"message": "User created successfully", "user": user.to_json()}), 201
# update user
def update_user(user_id):
    user = UserService.get_user(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 200
    data = request.get_json()
    updated_user = UserService.update_user(user, data)
    return jsonify({"message": "User updated successfully", "user": updated_user.to_json()}), 200
# delete user
def delete_user(user_id):
    user = UserService.get_user(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 200
    UserService.delete_user(user)
    return jsonify({"message": "User deleted successfully"}), 200
