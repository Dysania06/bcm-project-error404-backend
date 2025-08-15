from flask import Blueprint, request, jsonify
from models.user_model import User
from models.models import db
from schemas.user_schema import user_schema, users_schema

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify(users_schema.dump(users))

@user_bp.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(user_schema.dump(user))
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(**data)
    new_user.save_to_db()
    return jsonify(user_schema.dump(new_user)), 201

@user_bp.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    user = User.get_by_id(id)
    if user:
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        user.save_to_db()
        return jsonify(user_schema.dump(user))
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = User.get_by_id(id)
    if user:
        user.delete_from_db()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
