from flask import Blueprint, request, jsonify
from models.documents_tags_model import DocumentsTags
from schemas.documents_tags_schema import document_tag_schema, documents_tags_schema

documents_tags_bp = Blueprint('documents_tags_bp', __name__)

@documents_tags_bp.route('/documents_tags', methods=['GET'])
def get_documents_tags():
    return jsonify(documents_tags_schema.dump(DocumentsTags.get_all()))

@documents_tags_bp.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['GET'])
def get_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    return jsonify(document_tag_schema.dump(doc_tag)) if doc_tag else (jsonify({'message': 'Document Tag not found'}), 404)

@documents_tags_bp.route('/documents_tags', methods=['POST'])
def create_document_tag():
    new_doc_tag = DocumentsTags(**request.get_json())
    new_doc_tag.save_to_db()
    return jsonify(document_tag_schema.dump(new_doc_tag)), 201

@documents_tags_bp.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['DELETE'])
def delete_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    if not doc_tag:
        return jsonify({'message': 'Document Tag not found'}), 404
    doc_tag.delete_from_db()
    return jsonify({'message': 'Document Tag deleted successfully'})
