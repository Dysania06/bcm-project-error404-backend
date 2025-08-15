from . import ma
from models.rating_model import Rating

class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        load_instance = True

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)
