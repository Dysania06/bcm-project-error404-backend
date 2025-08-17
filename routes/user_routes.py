from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserController.get_all()
    return jsonify([u.to_json() for u in users]), 200

@user_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = UserController.get_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user.to_json()), 200

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = UserController.create(data)
    return jsonify(user.to_json()), 201

@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    user = UserController.get_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.json
    user = UserController.update(user, data)
    return jsonify(user.to_json()), 200

@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserController.get_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    UserController.delete(user)
    return jsonify({"message": "User deleted"}), 200
