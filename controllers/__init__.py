from .user_controller import user_bp
from .post_controller import post_bp
from .document_controller import document_bp
from .comment_controller import comment_bp
from .tag_controller import tag_bp
from .rating_controller import rating_bp
from .bookmark_controller import bookmark_bp

__all__ = [
    "user_bp",
    "post_bp",
    "document_bp",
    "comment_bp",
    "tag_bp",
    "rating_bp",
    "bookmark_bp"
]
