from flask_restful import Resource, reqparse
from models.tag_model import Tag

class TagsResource(Resource):
    def get(self):
        tags = Tag.get_all()
        return {'tags': tags}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tag_id', type=str, required=True, help='Tag ID cannot be blank')
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        args = parser.parse_args()

        tag_id = Tag.create(
            args['tag_id'],
            args['name']
        )
        return {'message': 'Tag created successfully', 'id': tag_id}, 201

class TagResource(Resource):
    def get(self, tag_id):
        tag = Tag.get_by_id(tag_id)
        if tag:
            return {'tag': tag}, 200
        return {'message': 'Tag not found'}, 404

    def put(self, tag_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=False)
        args = parser.parse_args()

        affected_rows = Tag.update(
            tag_id,
            args['name']
        )
        if affected_rows:
            return {'message': 'Tag updated successfully'}, 200
        return {'message': 'Tag not found or no changes made'}, 404

    def delete(self, tag_id):
        affected_rows = Tag.delete(tag_id)
        if affected_rows:
            return {'message': 'Tag deleted successfully'}, 200
        return {'message': 'Tag not found'}, 404