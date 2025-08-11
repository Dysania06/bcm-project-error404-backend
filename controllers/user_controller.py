from flask_restful import Resource, reqparse
from models.user_model import User

class UsersResource(Resource):
    def get(self):
        users = User.get_all()
        return {'users': users}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help='ID cannot be blank')
        parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
        parser.add_argument('user_password', type=str, required=True, help='Password cannot be blank')
        parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        parser.add_argument('phone', type=str, required=False)
        parser.add_argument('age', type=int, required=False)
        parser.add_argument('department', type=str, required=False)
        args = parser.parse_args()

        user_id = User.create(
            args['id'],
            args['username'],
            args['user_password'],
            args['email'],
            args['phone'],
            args['age'],
            args['department']
        )
        return {'message': 'User created successfully', 'id': user_id}, 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            return {'user': user}, 200
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=False)
        parser.add_argument('user_password', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('phone', type=str, required=False)
        parser.add_argument('age', type=int, required=False)
        parser.add_argument('department', type=str, required=False)
        args = parser.parse_args()

        affected_rows = User.update(
            user_id,
            args['username'],
            args['user_password'],
            args['email'],
            args['phone'],
            args['age'],
            args['department']
        )
        if affected_rows:
            return {'message': 'User updated successfully'}, 200
        return {'message': 'User not found or no changes made'}, 404

    def delete(self, user_id):
        affected_rows = User.delete(user_id)
        if affected_rows:
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404