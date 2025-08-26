from flask import jsonify, request
from models.posts_tags_model import posts_tags
from models.models import db
#  get all posts_tags
def get_all_posts_tags():
    records = posts_tags.query.all()
    return jsonify([r.to_json() for r in records]), 200
# get posts_tags by id
def get_posts_tag(record_id):
    record = posts_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "PostsTags not found"}), 200
    return jsonify(record.to_json()), 200
# create posts_tags
def create_posts_tags():
    data = request.get_json()
    new_record = posts_tags(
        post_id=data.get("post_id"),
        tag_id=data.get("tag_id")
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "PostsTags created successfully", "record": new_record.to_json()}), 201
#  update posts_tags
def update_posts_tags(record_id):
    record = posts_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "PostsTags not found"}), 200
    data = request.get_json()
    record.post_id = data.get("post_id", record.post_id)
    record.tag_id = data.get("tag_id", record.tag_id)
    db.session.commit()
    return jsonify({"message": "PostsTags updated successfully", "record": record.to_json()}), 200
# delete posts_tags
def delete_posts_tags(record_id):
    record = posts_tags.query.get(record_id)
    if not record:
        return jsonify({"message": "PostsTags not found"}), 200
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "PostsTags deleted successfully"}), 200
