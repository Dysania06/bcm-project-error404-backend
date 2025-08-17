# routes/documents_tags_routes.py
from flask import Blueprint, jsonify
from controllers.documents_tags_controller import DocumentsTagsController

documents_tags_bp = Blueprint("documents_tags", __name__, url_prefix="/documents_tags")

@documents_tags_bp.route("/<int:document_id>/tags/<int:tag_id>", methods=["POST"])
def add_tag_to_document(document_id, tag_id):
    return jsonify(DocumentsTagsController.add_tag_to_document(document_id, tag_id))

@documents_tags_bp.route("/<int:document_id>/tags/<int:tag_id>", methods=["DELETE"])
def remove_tag_from_document(document_id, tag_id):
    return jsonify(DocumentsTagsController.remove_tag_from_document(document_id, tag_id))

@documents_tags_bp.route("/<int:document_id>/tags", methods=["GET"])
def get_tags_of_document(document_id):
    return jsonify(DocumentsTagsController.get_tags_of_document(document_id))

@documents_tags_bp.route("/tags/<int:tag_id>/documents", methods=["GET"])
def get_documents_of_tag(tag_id):
    return jsonify(DocumentsTagsController.get_documents_of_tag(tag_id))
