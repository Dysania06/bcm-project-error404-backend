from flask_restful import Resource, reqparse
from models.rating_model import Rating

class RatingsResource(Resource):
    def get(self):
        ratings = Rating.get_all()
        return {'ratings': ratings}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rating_id', type=str, required=True, help='Rating ID cannot be blank')
        parser.add_argument('star_rating', type=int, required=True, help='Star rating cannot be blank')
        parser.add_argument('rated_by', type=str, required=True, help='Rated by cannot be blank')
        parser.add_argument('document_id', type=str, required=True, help='Document ID cannot be blank')
        args = parser.parse_args()

        rating_id = Rating.create(
            args['rating_id'],
            args['star_rating'],
            args['rated_by'],
            args['document_id']
        )
        return {'message': 'Rating created successfully', 'id': rating_id}, 201

class RatingResource(Resource):
    def get(self, rating_id):
        rating = Rating.get_by_id(rating_id)
        if rating:
            return {'rating': rating}, 200
        return {'message': 'Rating not found'}, 404

    def put(self, rating_id):
        parser = reqparse.RequestParser()
        parser.add_argument('star_rating', type=int, required=False)
        args = parser.parse_args()

        affected_rows = Rating.update(
            rating_id,
            args['star_rating']
        )
        if affected_rows:
            return {'message': 'Rating updated successfully'}, 200
        return {'message': 'Rating not found or no changes made'}, 404

    def delete(self, rating_id):
        affected_rows = Rating.delete(rating_id)
        if affected_rows:
            return {'message': 'Rating deleted successfully'}, 200
        return {'message': 'Rating not found'}, 404