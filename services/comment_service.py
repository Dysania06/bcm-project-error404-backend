import uuid
from datetime import datetime
from models.comment_model import Comment
from repositories.comment_repository import CommentRepository
# service for Comment model
class CommentService:
    @staticmethod
    def get_all_comments():
        return [c.to_json() for c in CommentRepository.get_all()]
#   get comment by id
    @staticmethod
    def get_comment_by_id(comment_id):
        comment = CommentRepository.get_by_id(comment_id)
        return comment.to_json() if comment else None
# create a new comment
    @staticmethod
    def create_comment(data):
        if not data.get("content") or not data.get("post_id") or not data.get("created_by"):
            return None, "Missing required fields"
        new_comment = Comment(
            id=str(uuid.uuid4()),
            content=data.get("content"),
            post_id=data.get("post_id"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        CommentRepository.create(new_comment)
        return new_comment.to_json(), None
# update an existing comment
    @staticmethod
    def update_comment(comment_id, data):
        comment = CommentRepository.get_by_id(comment_id)
        if not comment:
            return None
        # only content can be updated
        if "content" in data:
            comment.content = data["content"]
        comment.updated_at = datetime.utcnow()
        # save changes
        CommentRepository.update()
        return comment.to_json()
# delete a comment
    @staticmethod
    def delete_comment(comment_id):
        comment = CommentRepository.get_by_id(comment_id)
        if not comment:
            return None
        CommentRepository.delete(comment)
        return True
