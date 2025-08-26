from schemas import ma
from models.rating_model import Rating
# rating schema
class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        load_instance = True
# single and multiple rating schema
rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)
