from models.user_model import User
from models.models import db
# repository for User model
class UserRepository:
    @staticmethod
    def get_all():
        return User.query.all()
#   get user by id
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
# get user by username
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
# create a new user
    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user
# update an existing user
    @staticmethod
    def update():
        db.session.commit()
# delete a user
    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
