from models.models import db

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.String(50), primary_key=True)
    content = db.Column(db.Text)
    commented_by = db.Column(db.String(50), db.ForeignKey('users.id'))
    post_id = db.Column(db.String(50), db.ForeignKey('posts.post_id'))
    document_id = db.Column(db.String(50), db.ForeignKey('documents.document_id'))

    # Relationships
    user = db.relationship('User', backref='comments')
    post = db.relationship('Post', backref='comments')
    document = db.relationship('Document', backref='comments')

    def __init__(self, comment_id, content, commented_by, post_id=None, document_id=None):
        self.comment_id = comment_id
        self.content = content
        self.commented_by = commented_by
        self.post_id = post_id
        self.document_id = document_id

    def json(self):
        return {
            'comment_id': self.comment_id,
            'content': self.content,
            'commented_by': self.commented_by,
            'post_id': self.post_id,
            'document_id': self.document_id
        }

    @classmethod
    def find_by_id(cls, comment_id):
        return cls.query.filter_by(comment_id=comment_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class CommentService:
    @staticmethod
    def add_comment(comment_id, content, commented_by, post_id=None, document_id=None):
        comment = Comment(
            comment_id=comment_id,
            content=content,
            commented_by=commented_by,
            post_id=post_id,
            document_id=document_id
        )
        comment.save_to_db()
        return comment