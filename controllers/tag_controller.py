from flask import jsonify, request
from services.tag_service import TagService
# get all tags
def get_all_tags():
    tags = TagService.get_all_tags()
    return jsonify([tag.to_json() for tag in tags]), 200
#  get tag by id
def get_tag(tag_id):
    tag = TagService.get_tag(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 200
    return jsonify(tag.to_json()), 200
# create tag
def create_tag():
    data = request.get_json()
    tag = TagService.create_tag(data)
    return jsonify({"message": "Tag created successfully", "tag": tag.to_json()}), 201
# update tag
def update_tag(tag_id):
    tag = TagService.get_tag(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 200
    data = request.get_json()
    updated_tag = TagService.update_tag(tag, data)
    return jsonify({"message": "Tag updated successfully", "tag": updated_tag.to_json()}), 200
# delete tag
def delete_tag(tag_id):
    tag = TagService.get_tag(tag_id)
    if not tag:
        return jsonify({"message": "Tag not found"}), 200
    TagService.delete_tag(tag)
    return jsonify({"message": "Tag deleted successfully"}), 200
