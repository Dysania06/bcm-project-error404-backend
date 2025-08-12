# File: documents_api.py
from flask import Blueprint, request, jsonify
from models.document_model import Document
from models.models import db

documents_bp = Blueprint('documents', __name__)

# Lấy tất cả document
@documents_bp.route('/documents', methods=['GET'])
def get_documents():
    documents = Document.get_all()
    return jsonify([doc.to_json() for doc in documents])

# Lấy document theo id
@documents_bp.route('/documents/<string:document_id>', methods=['GET'])
def get_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        return jsonify(document.to_json())
    return jsonify({'message': 'Document not found'}), 404

# Thêm document mới
@documents_bp.route('/documents', methods=['POST'])
def create_document():
    data = request.get_json()
    new_document = Document(
        document_id=data['document_id'],
        title=data['title'],
        content=data['content'],
        uploaded_by=data['uploaded_by']
    )
    new_document.save_to_db()
    return jsonify({'message': 'Document created successfully'}), 201

# Cập nhật document
@documents_bp.route('/documents/<string:document_id>', methods=['PUT'])
def update_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        data = request.get_json()
        document.title = data.get('title', document.title)
        document.content = data.get('content', document.content)
        document.uploaded_by = data.get('uploaded_by', document.uploaded_by)
        document.save_to_db()
        return jsonify({'message': 'Document updated successfully'})
    return jsonify({'message': 'Document not found'}), 404

# Xóa document
@documents_bp.route('/documents/<string:document_id>', methods=['DELETE'])
def delete_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        document.delete_from_db()
        return jsonify({'message': 'Document deleted successfully'})
    return jsonify({'message': 'Document not found'}), 404