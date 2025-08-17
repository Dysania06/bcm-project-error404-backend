from flask import Blueprint, request, jsonify
from controllers.tag_controller import TagController

tag_bp = Blueprint("tag_bp", __name__, url_prefix="/tags")

@tag_bp.route("/", methods=["GET"])
def get_tags():
    tags = TagController.get_all()
    return jsonify([t.to_json() for t in tags]), 200

@tag_bp.route("/<tag_id>", methods=["GET"])
def get_tag(tag_id):
    tag = TagController.get_by_id(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 404
    return jsonify(tag.to_json()), 200

@tag_bp.route("/", methods=["POST"])
def create_tag():
    data = request.json
    tag = TagController.create(data)
    return jsonify(tag.to_json()), 201

@tag_bp.route("/<tag_id>", methods=["PUT"])
def update_tag(tag_id):
    tag = TagController.get_by_id(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 404
    data = request.json
    tag = TagController.update(tag, data)
    return jsonify(tag.to_json()), 200

@tag_bp.route("/<tag_id>", methods=["DELETE"])
def delete_tag(tag_id):
    tag = TagController.get_by_id(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 404
    TagController.delete(tag)
    return jsonify({"message": "Tag deleted"}), 200
