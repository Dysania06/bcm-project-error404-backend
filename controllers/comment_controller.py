from flask_restful import Resource, reqparse
from models.comment_model import Comment  # Đảm bảo import model tương ứng

class CommentsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('content', type=str, required=True)
    parser.add_argument('user_id', type=int, required=True)
    parser.add_argument('post_id', type=int, required=True)  # Hoặc document_id tùy model
    
    def get(self, comment_id=None):
        if comment_id:
            comment = Comment.find_by_id(comment_id)
            if comment:
                return comment.json()
            return {'message': 'Comment not found'}, 404
        return {'comments': [comment.json() for comment in Comment.query.all()]}
    
    def post(self):
        data = CommentsResource.parser.parse_args()
        comment = Comment(**data)
        try:
            comment.save_to_db()
            return comment.json(), 201
        except:
            return {'message': 'An error occurred'}, 500
    
    def put(self, comment_id):
        # Thêm logic update nếu cần
        pass
    
    def delete(self, comment_id):
        # Thêm logic delete nếu cần
        pass