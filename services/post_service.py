import uuid
from datetime import datetime
from models.post_model import Post
from repositories.post_repository import PostRepository
# Post service class
class PostService:
    @staticmethod
    def get_all_posts():
        return PostRepository.get_all()
# Get post by id
    @staticmethod
    def get_post(post_id):
        return PostRepository.get_by_id(post_id)
# Create new post
    @staticmethod
    def create_post(data):
        new_post = Post(
            id=str(uuid.uuid4()),
            title=data.get("title"),
            content=data.get("content"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return PostRepository.create(new_post)
# Update post
    @staticmethod
    def update_post(post, data):
        post.title = data.get("title", post.title)
        post.content = data.get("content", post.content)
        post.updated_at = datetime.utcnow()
        PostRepository.update()
        return post
# Delete post
    @staticmethod
    def delete_post(post):
        PostRepository.delete(post)
