from flask_restful import Resource, reqparse
from models.post_model import Post

class PostsResource(Resource):
    def get(self):
        posts = Post.get_all()
        return {'posts': posts}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('post_id', type=str, required=True, help='Post ID cannot be blank')
        parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
        parser.add_argument('content', type=str, required=True, help='Content cannot be blank')
        parser.add_argument('posted_by', type=str, required=True, help='Posted by cannot be blank')
        args = parser.parse_args()

        post_id = Post.create(
            args['post_id'],
            args['title'],
            args['content'],
            args['posted_by']
        )
        return {'message': 'Post created successfully', 'id': post_id}, 201

class PostResource(Resource):
    def get(self, post_id):
        post = Post.get_by_id(post_id)
        if post:
            return {'post': post}, 200
        return {'message': 'Post not found'}, 404

    def put(self, post_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=False)
        parser.add_argument('content', type=str, required=False)
        args = parser.parse_args()

        affected_rows = Post.update(
            post_id,
            args['title'],
            args['content']
        )
        if affected_rows:
            return {'message': 'Post updated successfully'}, 200
        return {'message': 'Post not found or no changes made'}, 404

    def delete(self, post_id):
        affected_rows = Post.delete(post_id)
        if affected_rows:
            return {'message': 'Post deleted successfully'}, 200
        return {'message': 'Post not found'}, 404