from flask_restful import Resource, reqparse
from models.bookmark_model import Bookmark

class BookmarkResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        parser.add_argument('document_id', required=True)
        args = parser.parse_args()

        Bookmark.add_bookmark(args['user_id'], args['document_id'])
        return {'message': 'Document bookmarked'}, 201