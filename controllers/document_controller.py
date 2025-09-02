from flask import request, jsonify
from services.document_service import DocumentService
# get all documents
def get_all_documents():
    docs = DocumentService.get_all_documents()
    return jsonify(docs), 200
# get document by id
def get_document(document_id):
    doc = DocumentService.get_document_by_id(document_id)
    if not doc:
        return jsonify({"message": "Document not found"}), 404
    return jsonify(doc), 200
# create document
def create_document():
    data = request.get_json()
    new_doc, error = DocumentService.create_document(data)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Document created successfully", "document": new_doc}), 201
# update document
def update_document(document_id):
    data = request.get_json()
    updated_doc = DocumentService.update_document(document_id, data)
    if not updated_doc:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Document updated successfully", "document": updated_doc}), 200
# delete document
def delete_document(document_id):
    deleted = DocumentService.delete_document(document_id)
    if not deleted:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Document deleted successfully"}), 200
