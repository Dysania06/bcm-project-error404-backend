# File: tags_api.py
from flask import Blueprint, request, jsonify
from models.tag_model import Tag
from models.models import db

tags_bp = Blueprint('tags', __name__)

# Lấy tất cả tag
@tags_bp.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.get_all()
    return jsonify([tag.to_json() for tag in tags])

# Lấy tag theo id
@tags_bp.route('/tags/<string:tag_id>', methods=['GET'])
def get_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        return jsonify(tag.to_json())
    return jsonify({'message': 'Tag not found'}), 404

# Thêm tag mới
@tags_bp.route('/tags', methods=['POST'])
def create_tag():
    data = request.get_json()
    new_tag = Tag(
        tag_id=data['tag_id'],
        nameposts_tags=data['nameposts_tags']
    )
    new_tag.save_to_db()
    return jsonify({'message': 'Tag created successfully'}), 201

# Cập nhật tag
@tags_bp.route('/tags/<string:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        data = request.get_json()
        tag.nameposts_tags = data.get('nameposts_tags', tag.nameposts_tags)
        tag.save_to_db()
        return jsonify({'message': 'Tag updated successfully'})
    return jsonify({'message': 'Tag not found'}), 404

# Xóa tag
@tags_bp.route('/tags/<string:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        tag.delete_from_db()
        return jsonify({'message': 'Tag deleted successfully'})
    return jsonify({'message': 'Tag not found'}), 404