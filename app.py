from flask import Flask
# Import đối tượng db
from models.models import db

# Import tất cả các model từ các file riêng của chúng
from models.user_model import User
from models.document_model import Document
from models.comment_model import Comment
from models.bookmark_model import Bookmark
from models.document_tag_model import DocumentsTags
from models.post_model import Post
from models.post_tag_model import PostsTags
from models.rating_model import Rating
from models.tag_model import Tag

# Import tất cả các blueprint của API
from users_api import users_bp
from documents_api import documents_bp
from comments_api import comments_bp
from bookmarks_api import bookmarks_bp
from documents_tags_api import documents_tags_bp
from posts_api import posts_bp
from ratings_api import ratings_bp
from posts_tags_api import posts_tags_bp
from tags_api import tags_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:chien19102006%40@localhost/csdl_bit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Đăng ký các blueprints vào ứng dụng
app.register_blueprint(users_bp)
app.register_blueprint(documents_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(bookmarks_bp)
app.register_blueprint(documents_tags_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(ratings_bp)
app.register_blueprint(posts_tags_bp)
app.register_blueprint(tags_bp)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    with app.app_context():
        # Dòng này tạo tất cả các bảng trong cơ sở dữ liệu nếu chúng chưa tồn tại.
        db.create_all()
    app.run(debug=True)