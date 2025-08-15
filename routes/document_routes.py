from flask import Blueprint, request, jsonify
from models.document_model import Document
from schemas.document_schema import document_schema, documents_schema

document_bp = Blueprint('document_bp', __name__)

@document_bp.route('/documents', methods=['GET'])
def get_documents():
    return jsonify(documents_schema.dump(Document.get_all()))

@document_bp.route('/documents/<string:id>', methods=['GET'])
def get_document(id):
    document = Document.get_by_id(id)
    return jsonify(document_schema.dump(document)) if document else (jsonify({'message': 'Document not found'}), 404)

@document_bp.route('/documents', methods=['POST'])
def create_document():
    new_document = Document(**request.get_json())
    new_document.save_to_db()
    return jsonify(document_schema.dump(new_document)), 201

@document_bp.route('/documents/<string:id>', methods=['PUT'])
def update_document(id):
    document = Document.get_by_id(id)
    if not document:
        return jsonify({'message': 'Document not found'}), 404
    for k, v in request.get_json().items():
        setattr(document, k, v)
    document.save_to_db()
    return jsonify(document_schema.dump(document))

@document_bp.route('/documents/<string:id>', methods=['DELETE'])
def delete_document(id):
    document = Document.get_by_id(id)
    if not document:
        return jsonify({'message': 'Document not found'}), 404
    document.delete_from_db()
    return jsonify({'message': 'Document deleted successfully'})
