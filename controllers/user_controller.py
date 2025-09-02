from flask import request, jsonify
from services.user_service import UserService
# get all users
def get_all_users():
    users = UserService.get_all_users()
    return jsonify(users), 200
# get user by id
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user), 200
# create user
def create_user():
    data = request.get_json()
    new_user, error = UserService.create_user(data)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "User created successfully", "user": new_user}), 201
# update user
def update_user(user_id):
    data = request.get_json()
    updated_user = UserService.update_user(user_id, data)
    if not updated_user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User updated successfully", "user": updated_user}), 200
# delete user
def delete_user(user_id):
    deleted = UserService.delete_user(user_id)
    if not deleted:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
