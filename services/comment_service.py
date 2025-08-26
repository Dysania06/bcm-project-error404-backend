import uuid
from datetime import datetime
from models.comment_model import Comment
from repositories.comment_repository import CommentRepository
#  Comment service class
class CommentService:
    @staticmethod
    def get_all_comments():
        return CommentRepository.get_all()
#  Get comment by id
    @staticmethod
    def get_comment(comment_id):
        return CommentRepository.get_by_id(comment_id)
#  Create new comment
    @staticmethod
    def create_comment(data):
        new_comment = Comment(
            id=str(uuid.uuid4()),
            content=data.get("content"),
            created_by=data.get("created_by"),
            post_id=data.get("post_id"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return CommentRepository.create(new_comment)
#  Update comment
    @staticmethod
    def update_comment(comment, data):
        comment.content = data.get("content", comment.content)
        comment.updated_at = datetime.utcnow()
        CommentRepository.update()
        return comment
#  Delete comment
    @staticmethod
    def delete_comment(comment):
        CommentRepository.delete(comment)
