from flask_restful import Resource, reqparse
from models.document_model import Document

class DocumentsResource(Resource):
    def get(self):
        documents = Document.get_all()
        return {'documents': documents}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('document_id', type=str, required=True, help='Document ID cannot be blank')
        parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
        parser.add_argument('content', type=str, required=True, help='Content cannot be blank')
        parser.add_argument('password', type=str, required=True, help='Password cannot be blank')
        parser.add_argument('uploaded_by', type=str, required=True, help='Uploader ID cannot be blank')
        args = parser.parse_args()

        document_id = Document.create(
            args['document_id'],
            args['title'],
            args['content'],
            args['password'],
            args['uploaded_by']
        )
        return {'message': 'Document created successfully', 'id': document_id}, 201

class DocumentResource(Resource):
    def get(self, document_id):
        document = Document.get_by_id(document_id)
        if document:
            return {'document': document}, 200
        return {'message': 'Document not found'}, 404

    def put(self, document_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=False)
        parser.add_argument('content', type=str, required=False)
        parser.add_argument('password', type=str, required=False)
        args = parser.parse_args()

        affected_rows = Document.update(
            document_id,
            args['title'],
            args['content'],
            args['password']
        )
        if affected_rows:
            return {'message': 'Document updated successfully'}, 200
        return {'message': 'Document not found or no changes made'}, 404

    def delete(self, document_id):
        affected_rows = Document.delete(document_id)
        if affected_rows:
            return {'message': 'Document deleted successfully'}, 200
        return {'message': 'Document not found'}, 404