from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
from .document_model import Document
from .comment_model import Comment
from .bookmark_model import Bookmark
from .documents_tags_model import DocumentsTags
from .post_model import Post
from .posts_tags_model import PostsTags
from .rating_model import Rating
from .tag_model import Tag

__all__ = [
    'User',
    'Post',
    'Document',
    'Comment',
    'Tag',
    'Rating',
    'Bookmark'
]