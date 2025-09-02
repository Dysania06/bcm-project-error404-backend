import uuid
from models.rating_model import Rating
from repositories.rating_repository import RatingRepository
#   service for Rating model
class RatingService:
    @staticmethod
    def get_all_ratings():
        return RatingRepository.get_all()
#   get rating by id
    @staticmethod
    def get_rating(rating_id):
        return RatingRepository.get_by_id(rating_id)
# create a new rating
    @staticmethod
    def create_rating(data):
        new_rating = Rating(
            id=str(uuid.uuid4()),
            user_id=data.get("user_id"),
            post_id=data.get("post_id"),
            score=data.get("score")
        )
        return RatingRepository.create(new_rating)
# update an existing rating
    @staticmethod
    def update_rating(rating, data):
        rating.score = data.get("score", rating.score)
        RatingRepository.update()
        return rating
# delete a rating
    @staticmethod
    def delete_rating(rating):
        RatingRepository.delete(rating)
