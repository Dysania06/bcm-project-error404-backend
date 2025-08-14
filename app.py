import os
from models.models import db
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from models.models import db
from models.user_model import User
from models.post_model import Post
from models.bookmark_model import Bookmark
from models.comment_model import Comment
from models.document_model import Document
from models.documents_tags_model import DocumentsTags
from models.posts_tags_model import PostsTags
from models.rating_model import Rating
from models.tag_model import Tag


load_dotenv()  # Load biến môi trường từ file .env

app = Flask(__name__)

MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ===== USERS =====
@app.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify([user.to_json() for user in users])

@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(user.to_json())
    return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(**data)
    new_user.save_to_db()
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    user = User.get_by_id(id)
    if user:
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        user.save_to_db()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    user = User.get_by_id(id)
    if user:
        user.delete_from_db()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

# ===== POSTS =====
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.get_all()
    return jsonify([post.to_json() for post in posts])

@app.route('/posts/<string:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        return jsonify(post.to_json())
    return jsonify({'message': 'Post not found'}), 404

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(**data)
    new_post.save_to_db()
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts/<string:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        data = request.get_json()
        for key, value in data.items():
            setattr(post, key, value)
        post.save_to_db()
        return jsonify({'message': 'Post updated successfully'})
    return jsonify({'message': 'Post not found'}), 404

@app.route('/posts/<string:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.get_by_id(post_id)
    if post:
        post.delete_from_db()
        return jsonify({'message': 'Post deleted successfully'})
    return jsonify({'message': 'Post not found'}), 404

# ===== BOOKMARKS =====
@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    bookmarks = Bookmark.get_all()
    return jsonify([bookmark.to_json() for bookmark in bookmarks])

@app.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['GET'])
def get_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    if bookmark:
        return jsonify(bookmark.to_json())
    return jsonify({'message': 'Bookmark not found'}), 404

@app.route('/bookmarks', methods=['POST'])
def create_bookmark():
    data = request.get_json()
    new_bookmark = Bookmark(**data)
    new_bookmark.save_to_db()
    return jsonify({'message': 'Bookmark created successfully'}), 201

@app.route('/bookmarks/<string:document_id>/<string:user_id>', methods=['DELETE'])
def delete_bookmark(document_id, user_id):
    bookmark = Bookmark.query.get((document_id, user_id))
    if bookmark:
        bookmark.delete_from_db()
        return jsonify({'message': 'Bookmark deleted successfully'})
    return jsonify({'message': 'Bookmark not found'}), 404

# ===== COMMENTS =====
@app.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.get_all()
    return jsonify([comment.json() for comment in comments])

@app.route('/comments/<string:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        return jsonify(comment.json())
    return jsonify({'message': 'Comment not found'}), 404

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    new_comment = Comment(**data)
    new_comment.save_to_db()
    return jsonify({'message': 'Comment created successfully'}), 201

@app.route('/comments/<string:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        data = request.get_json()
        for key, value in data.items():
            setattr(comment, key, value)
        comment.save_to_db()
        return jsonify({'message': 'Comment updated successfully'})
    return jsonify({'message': 'Comment not found'}), 404

@app.route('/comments/<string:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = Comment.get_by_id(comment_id)
    if comment:
        comment.delete_from_db()
        return jsonify({'message': 'Comment deleted successfully'})
    return jsonify({'message': 'Comment not found'}), 404

# ===== DOCUMENTS =====
@app.route('/documents', methods=['GET'])
def get_documents():
    documents = Document.get_all()
    return jsonify([doc.to_json() for doc in documents])

@app.route('/documents/<string:document_id>', methods=['GET'])
def get_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        return jsonify(document.to_json())
    return jsonify({'message': 'Document not found'}), 404

@app.route('/documents', methods=['POST'])
def create_document():
    data = request.get_json()
    new_document = Document(**data)
    new_document.save_to_db()
    return jsonify({'message': 'Document created successfully'}), 201

@app.route('/documents/<string:document_id>', methods=['PUT'])
def update_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        data = request.get_json()
        for key, value in data.items():
            setattr(document, key, value)
        document.save_to_db()
        return jsonify({'message': 'Document updated successfully'})
    return jsonify({'message': 'Document not found'}), 404

@app.route('/documents/<string:document_id>', methods=['DELETE'])
def delete_document(document_id):
    document = Document.get_by_id(document_id)
    if document:
        document.delete_from_db()
        return jsonify({'message': 'Document deleted successfully'})
    return jsonify({'message': 'Document not found'}), 404

# ===== DOCUMENT TAGS =====
@app.route('/documents_tags', methods=['GET'])
def get_documents_tags():
    docs_tags = DocumentsTags.get_all()
    return jsonify([doc_tag.to_json() for doc_tag in docs_tags])

@app.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['GET'])
def get_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    if doc_tag:
        return jsonify(doc_tag.to_json())
    return jsonify({'message': 'Document Tag not found'}), 404

@app.route('/documents_tags', methods=['POST'])
def create_document_tag():
    data = request.get_json()
    new_doc_tag = DocumentsTags(**data)
    new_doc_tag.save_to_db()
    return jsonify({'message': 'Document Tag created successfully'}), 201

@app.route('/documents_tags/<string:document_id>/<string:tag_id>', methods=['DELETE'])
def delete_document_tag(document_id, tag_id):
    doc_tag = DocumentsTags.query.get((document_id, tag_id))
    if doc_tag:
        doc_tag.delete_from_db()
        return jsonify({'message': 'Document Tag deleted successfully'})
    return jsonify({'message': 'Document Tag not found'}), 404

# ===== POSTS TAGS =====
@app.route('/posts_tags', methods=['GET'])
def get_posts_tags():
    posts_tags = PostsTags.get_all()
    return jsonify([post_tag.to_json() for post_tag in posts_tags])

@app.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['GET'])
def get_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    if post_tag:
        return jsonify(post_tag.to_json())
    return jsonify({'message': 'Post Tag not found'}), 404

@app.route('/posts_tags', methods=['POST'])
def create_post_tag():
    data = request.get_json()
    new_post_tag = PostsTags(**data)
    new_post_tag.save_to_db()
    return jsonify({'message': 'Post Tag created successfully'}), 201

@app.route('/posts_tags/<string:post_id>/<string:tag_id>', methods=['DELETE'])
def delete_post_tag(post_id, tag_id):
    post_tag = PostsTags.query.get((post_id, tag_id))
    if post_tag:
        post_tag.delete_from_db()
        return jsonify({'message': 'Post Tag deleted successfully'})
    return jsonify({'message': 'Post Tag not found'}), 404

# ===== RATINGS =====
@app.route('/ratings', methods=['GET'])
def get_ratings():
    ratings = Rating.get_all()
    return jsonify([rating.to_json() for rating in ratings])

@app.route('/ratings/<string:rating_id>', methods=['GET'])
def get_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        return jsonify(rating.to_json())
    return jsonify({'message': 'Rating not found'}), 404

@app.route('/ratings', methods=['POST'])
def create_rating():
    data = request.get_json()
    new_rating = Rating(**data)
    new_rating.save_to_db()
    return jsonify({'message': 'Rating created successfully'}), 201

@app.route('/ratings/<string:rating_id>', methods=['PUT'])
def update_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        data = request.get_json()
        for key, value in data.items():
            setattr(rating, key, value)
        rating.save_to_db()
        return jsonify({'message': 'Rating updated successfully'})
    return jsonify({'message': 'Rating not found'}), 404

@app.route('/ratings/<string:rating_id>', methods=['DELETE'])
def delete_rating(rating_id):
    rating = Rating.get_by_id(rating_id)
    if rating:
        rating.delete_from_db()
        return jsonify({'message': 'Rating deleted successfully'})
    return jsonify({'message': 'Rating not found'}), 404

# ===== TAGS =====
@app.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.get_all()
    return jsonify([tag.to_json() for tag in tags])

@app.route('/tags/<string:tag_id>', methods=['GET'])
def get_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        return jsonify(tag.to_json())
    return jsonify({'message': 'Tag not found'}), 404

@app.route('/tags', methods=['POST'])
def create_tag():
    data = request.get_json()
    new_tag = Tag(**data)
    new_tag.save_to_db()
    return jsonify({'message': 'Tag created successfully'}), 201

@app.route('/tags/<string:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        data = request.get_json()
        for key, value in data.items():
            setattr(tag, key, value)
        tag.save_to_db()
        return jsonify({'message': 'Tag updated successfully'})
    return jsonify({'message': 'Tag not found'}), 404

@app.route('/tags/<string:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    tag = Tag.get_by_id(tag_id)
    if tag:
        tag.delete_from_db()
        return jsonify({'message': 'Tag deleted successfully'})
    return jsonify({'message': 'Tag not found'}), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
