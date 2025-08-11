# File: users_api.py
from flask import Blueprint, request, jsonify
from models.user_model import User
from models.models import db

users_bp = Blueprint('users', __name__)

# Lấy tất cả user
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify([user.to_json() for user in users])

# Lấy user theo id
@users_bp.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(user.to_json())
    return jsonify({'message': 'User not found'}), 404

# Thêm user mới
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        id=data['id'],
        username=data['username'],
        user_password=data['user_password'],
        email=data['email'],
        phone=data['phone'],
        age=data['age'],
        department=data['department']
    )
    new_user.save_to_db()
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

# Cập nhật user
@users_bp.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    user = User.get_by_id(id)
    if user:
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.user_password = data.get('user_password', user.user_password)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.age = data.get('age', user.age)
        user.department = data.get('department', user.department)
        user.save_to_db()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

# Xóa user
@users_bp.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = User.get_by_id(id)
    if user:
        user.delete_from_db()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404