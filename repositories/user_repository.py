from models.user_model import User, db
# user repository
class UserRepository:
    @staticmethod
    def get_all():
        return User.query.all()
# get user by id
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
# get user by email
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
# create user
    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user
# update user
    @staticmethod
    def update():
        db.session.commit()
# delete user
    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
