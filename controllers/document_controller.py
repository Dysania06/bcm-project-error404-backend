from flask import jsonify, request
from services.document_service import DocumentService
# get all documents
def get_all_documents():
    documents = DocumentService.get_all_documents()
    return jsonify([doc.to_json() for doc in documents]), 200
# get document by id
def get_document(document_id):
    document = DocumentService.get_document(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 200
    return jsonify(document.to_json()), 200
# create document
def create_document():
    data = request.get_json()
    document = DocumentService.create_document(data)
    return jsonify({"message": "Document created successfully", "document": document.to_json()}), 201
# update document
def update_document(document_id):
    document = DocumentService.get_document(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 200
    data = request.get_json()
    updated_document = DocumentService.update_document(document, data)
    return jsonify({"message": "Document updated successfully", "document": updated_document.to_json()}), 200
# delete document
def delete_document(document_id):
    document = DocumentService.get_document(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 200
    DocumentService.delete_document(document)
    return jsonify({"message": "Document deleted successfully"}), 200
