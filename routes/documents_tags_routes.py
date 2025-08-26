from flask import Blueprint
from controllers import documents_tags_controller
# create blueprint for documents_tags
documents_tags_bp = Blueprint("documents_tags_bp", __name__, url_prefix="/documents_tags")
# call controller from routes
documents_tags_bp.route("/", methods=["GET"])(documents_tags_controller.get_all_documents_tags)
documents_tags_bp.route("/<record_id>", methods=["GET"])(documents_tags_controller.get_documents_tags)
documents_tags_bp.route("/", methods=["POST"])(documents_tags_controller.create_documents_tags)
documents_tags_bp.route("/<record_id>", methods=["PUT"])(documents_tags_controller.update_documents_tags)
documents_tags_bp.route("/<record_id>", methods=["DELETE"])(documents_tags_controller.delete_documents_tags)
