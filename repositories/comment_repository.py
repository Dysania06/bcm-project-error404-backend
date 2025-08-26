from models.comment_model import Comment, db
#  comment repository
class CommentRepository:
    @staticmethod
    def get_all():
        return Comment.query.all()
#  get comment by id
    @staticmethod
    def get_by_id(comment_id):
        return Comment.query.get(comment_id)
# create comment
    @staticmethod
    def create(comment):
        db.session.add(comment)
        db.session.commit()
        return comment
# update comment
    @staticmethod
    def update():
        db.session.commit()
# delete comment
    @staticmethod
    def delete(comment):
        db.session.delete(comment)
        db.session.commit()
