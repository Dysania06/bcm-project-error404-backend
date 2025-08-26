import uuid
from models.rating_model import Rating
from repositories.rating_repository import RatingRepository
# Rating service class
class RatingService:
    @staticmethod
    def get_all_ratings():
        return RatingRepository.get_all()
# Get rating by id
    @staticmethod
    def get_rating(rating_id):
        return RatingRepository.get_by_id(rating_id)
# Create new rating
    @staticmethod
    def create_rating(data):
        new_rating = Rating(
            id=str(uuid.uuid4()),
            user_id=data.get("user_id"),
            post_id=data.get("post_id"),
            score=data.get("score")
        )
        return RatingRepository.create(new_rating)
# Update rating
    @staticmethod
    def update_rating(rating, data):
        rating.score = data.get("score", rating.score)
        RatingRepository.update()
        return rating
# Delete rating
    @staticmethod
    def delete_rating(rating):
        RatingRepository.delete(rating)
