from flask import Blueprint
from controllers import document_controller
# create blueprint for document
document_bp = Blueprint("document_bp", __name__, url_prefix="/documents")
# call controller from routes
document_bp.route("/", methods=["GET"])(document_controller.get_all_documents)
document_bp.route("/<document_id>", methods=["GET"])(document_controller.get_document)
document_bp.route("/", methods=["POST"])(document_controller.create_document)
document_bp.route("/<document_id>", methods=["PUT"])(document_controller.update_document)
document_bp.route("/<document_id>", methods=["DELETE"])(document_controller.delete_document)
