from flask import jsonify, request
from models.documents_tags_model import documents_tags
from models.models import db

#  get all documents_tags
def get_all_documents_tags():
    records = documents_tags.query.all()
    return jsonify([r.to_json() for r in records]), 200

# get documents_tags by id
def get_documents_tags(record_id):
    record = documents_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "DocumentsTags not found"}),200
    return jsonify(record.to_json()), 200

# create documents_tags
def create_documents_tags():
    data = request.get_json()
    try:
        new_record = documents_tags(
            document_id=data.get("document_id"),
            tag_id=data.get("tag_id")
        )
        db.session.add(new_record)
        db.session.commit()
        return jsonify({"message": "DocumentsTags created successfully", "record": new_record.to_json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# update documents_tags
def update_documents_tags(record_id):
    record = documents_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "DocumentsTags not found"}), 200

    data = request.get_json()
    try:
        record.document_id = data.get("document_id", record.document_id)
        record.tag_id = data.get("tag_id", record.tag_id)
        db.session.commit()
        return jsonify({"message": "DocumentsTags updated successfully", "record": record.to_json()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# delete documents_tags
def delete_documents_tags(record_id):
    record = documents_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "DocumentsTags not found"}), 200

    try:
        db.session.delete(record)
        db.session.commit()
        return jsonify({"message": "DocumentsTags deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
