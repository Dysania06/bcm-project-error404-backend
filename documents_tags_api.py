# File: documents_tags_api.py
from flask import Blueprint, request, jsonify
from models.document_tag_model import DocumentsTags
from models.models import db

documents_tags_bp = Blueprint('documents_tags', __name__)

# Lấy tất cả document_tag
@documents_tags_bp.route('/documents_tags', methods=['GET'])
def get_documents_tags():
    docs_tags = DocumentsTags.get_all()
    return jsonify([doc_tag.to_json() for doc_tag in docs_tags])

# Lấy document_tag theo document_id và tag_id
@documents_tags_bp.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['GET'])
def get_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    if doc_tag:
        return jsonify(doc_tag.to_json())
    return jsonify({'message': 'Document Tag not found'}), 404

# Thêm document_tag mới
@documents_tags_bp.route('/documents_tags', methods=['POST'])
def create_document_tag():
    data = request.get_json()
    new_doc_tag = DocumentsTags(
        document_id=data['document_id'],
        tag_id=data['tag_id']
    )
    new_doc_tag.save_to_db()
    return jsonify({'message': 'Document Tag created successfully'}), 201

# Xóa document_tag
@documents_tags_bp.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['DELETE'])
def delete_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    if doc_tag:
        doc_tag.delete_from_db()
        return jsonify({'message': 'Document Tag deleted successfully'})
    return jsonify({'message': 'Document Tag not found'}), 404