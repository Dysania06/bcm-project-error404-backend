from models.rating_model import Rating, db
# repository for Rating model
class RatingRepository:
    @staticmethod
    def get_all():
        return Rating.query.all()
#   get rating by id
    @staticmethod
    def get_by_id(rating_id):
        return Rating.query.get(rating_id)
# create a new rating
    @staticmethod
    def create(rating):
        db.session.add(rating)
        db.session.commit()
        return rating
# update an existing rating
    @staticmethod
    def update():
        db.session.commit()
# delete a rating
    @staticmethod
    def delete(rating):
        db.session.delete(rating)
        db.session.commit()
