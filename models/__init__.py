from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from .user_model import User
from .document_model import Document
from .comment_model import Comment
from .bookmark_model import Bookmark
from .post_model import Post
from .rating_model import Rating
from .tag_model import Tag 
from .documents_tags_model import documents_tags
from .posts_tags_model import posts_tags

__all__ = [
    'User',
    'Post',
    'Document',
    'Comment',
    'Tag',
    'Rating',
    'Bookmark'
]
