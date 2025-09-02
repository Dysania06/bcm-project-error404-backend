from models.comment_model import Comment
from models.models import db
# repository for Comment model
class CommentRepository:
    @staticmethod
    def get_all():
        return Comment.query.all()
#   get comment by id
    @staticmethod
    def get_by_id(comment_id):
        return Comment.query.get(comment_id)
# create a new comment
    @staticmethod
    def create(comment):
        db.session.add(comment)
        db.session.commit()
        return comment
# update an existing comment
    @staticmethod
    def update():
        db.session.commit()
# delete a comment
    @staticmethod
    def delete(comment):
        db.session.delete(comment)
        db.session.commit()
