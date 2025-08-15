from flask import Blueprint, request, jsonify
from models.tag_model import Tag
from schemas.tag_schema import tag_schema, tags_schema

tag_bp = Blueprint('tag_bp', __name__)

@tag_bp.route('/tags', methods=['GET'])
def get_tags():
    return jsonify(tags_schema.dump(Tag.get_all()))

@tag_bp.route('/tags/<string:id>', methods=['GET'])
def get_tag(id):
    tag = Tag.get_by_id(id)
    return jsonify(tag_schema.dump(tag)) if tag else (jsonify({'message': 'Tag not found'}), 404)

@tag_bp.route('/tags', methods=['POST'])
def create_tag():
    new_tag = Tag(**request.get_json())
    new_tag.save_to_db()
    return jsonify(tag_schema.dump(new_tag)), 201

@tag_bp.route('/tags/<string:id>', methods=['PUT'])
def update_tag(id):
    tag = Tag.get_by_id(id)
    if not tag:
        return jsonify({'message': 'Tag not found'}), 404
    for k, v in request.get_json().items():
        setattr(tag, k, v)
    tag.save_to_db()
    return jsonify(tag_schema.dump(tag))

@tag_bp.route('/tags/<string:id>', methods=['DELETE'])
def delete_tag(id):
    tag = Tag.get_by_id(id)
    if not tag:
        return jsonify({'message': 'Tag not found'}), 404
    tag.delete_from_db()
    return jsonify({'message': 'Tag deleted successfully'})
