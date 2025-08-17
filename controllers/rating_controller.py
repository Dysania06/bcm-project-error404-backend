from models import Rating, db

class RatingController:
    @staticmethod
    def get_all():
        return Rating.query.all()

    @staticmethod
    def get_by_id(rating_id):
        return Rating.query.get(rating_id)

    @staticmethod
    def create(data):
        new_rating = Rating(**data)
        db.session.add(new_rating)
        db.session.commit()
        return new_rating

    @staticmethod
    def update(rating, data):
        for key, value in data.items():
            setattr(rating, key, value)
        db.session.commit()
        return rating

    @staticmethod
    def delete(rating):
        db.session.delete(rating)
        db.session.commit()
