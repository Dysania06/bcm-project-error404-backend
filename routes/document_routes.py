from flask import Blueprint, request, jsonify
from controllers.document_controller import DocumentController

document_bp = Blueprint("document_bp", __name__, url_prefix="/documents")

@document_bp.route("/", methods=["GET"])
def get_documents():
    documents = DocumentController.get_all()
    return jsonify([d.to_json() for d in documents]), 200

@document_bp.route("/<document_id>", methods=["GET"])
def get_document(document_id):
    document = DocumentController.get_by_id(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 404
    return jsonify(document.to_json()), 200

@document_bp.route("/", methods=["POST"])
def create_document():
    data = request.json
    document = DocumentController.create(data)
    return jsonify(document.to_json()), 201

@document_bp.route("/<document_id>", methods=["PUT"])
def update_document(document_id):
    document = DocumentController.get_by_id(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 404
    data = request.json
    document = DocumentController.update(document, data)
    return jsonify(document.to_json()), 200

@document_bp.route("/<document_id>", methods=["DELETE"])
def delete_document(document_id):
    document = DocumentController.get_by_id(document_id)
    if not document:
        return jsonify({"message": "Document not found"}), 404
    DocumentController.delete(document)
    return jsonify({"message": "Document deleted"}), 200
