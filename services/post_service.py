import uuid
from datetime import datetime
from models.post_model import Post
from repositories.post_repository import PostRepository
# service for Post model
class PostService:
    @staticmethod
    def get_all_posts():
        return [p.to_json() for p in PostRepository.get_all()]
#   get post by id
    @staticmethod
    def get_post_by_id(post_id):
        post = PostRepository.get_by_id(post_id)
        return post.to_json() if post else None
# create a new post
    @staticmethod
    def create_post(data):
        if not data.get("title") or not data.get("content") or not data.get("created_by"):
            return None, "Missing required fields"

        new_post = Post(
            id=str(uuid.uuid4()),
            title=data.get("title"),
            content=data.get("content"),
            created_by=data.get("created_by"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        PostRepository.create(new_post)
        return new_post.to_json(), None
#   update an existing post
    @staticmethod
    def update_post(post_id, data):
        post = PostRepository.get_by_id(post_id)
        if not post:
            return None

        if "title" in data:
            post.title = data["title"]
        if "content" in data:
            post.content = data["content"]

        post.updated_at = datetime.utcnow()
        PostRepository.update()
        return post.to_json()
#   delete a post
    @staticmethod
    def delete_post(post_id):
        post = PostRepository.get_by_id(post_id)
        if not post:
            return None
        PostRepository.delete(post)
        return True
