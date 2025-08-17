from models import Comment, db

class CommentController:
    @staticmethod
    def get_all():
        return Comment.query.all()

    @staticmethod
    def get_by_id(comment_id):
        return Comment.query.get(comment_id)

    @staticmethod
    def create(data):
        new_comment = Comment(**data)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    @staticmethod
    def update(comment, data):
        for key, value in data.items():
            setattr(comment, key, value)
        db.session.commit()
        return comment

    @staticmethod
    def delete(comment):
        db.session.delete(comment)
        db.session.commit()
