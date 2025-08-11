from .user_controller import UserResource, UsersResource
from .post_controller import PostResource, PostsResource
from .document_controller import DocumentResource, DocumentsResource
from .comment_controller import CommentsResource
from .tag_controller import TagResource, TagsResource
from .rating_controller import RatingResource, RatingsResource
from .bookmark_controller import BookmarkResource, BookmarksResource

__all__ = [
    'UserResource',
    'UsersResource',
    'PostResource',
    'PostsResource',
    'DocumentResource',
    'DocumentsResource',
    'CommentsResource',
    'TagResource',
    'TagsResource',
    'RatingResource',
    'RatingsResource',
    'BookmarkResource',
    'BookmarksResource'
]