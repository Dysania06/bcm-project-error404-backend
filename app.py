import os
from flask import Flask
from dotenv import load_dotenv
from models.models import db
from schemas import ma

# Import các route blueprint
from routes.user_routes import user_bp
from routes.post_routes import post_bp
from routes.comment_routes import comment_bp
from routes.bookmark_routes import bookmark_bp
from routes.document_routes import document_bp
from routes.documents_tags_routes import documents_tags_bp
from routes.posts_tags_routes import posts_tags_bp
from routes.rating_routes import rating_bp
from routes.tag_routes import tag_bp

load_dotenv()

app = Flask(__name__)

# Config MySQL từ .env
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DB = os.getenv('MYSQL_DB')
# Encode password for URL
import urllib.parse
password_encoded = urllib.parse.quote_plus(MYSQL_PASSWORD)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db + marshmallow
db.init_app(app)
ma.init_app(app)

# Register blueprint
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(bookmark_bp)
app.register_blueprint(document_bp)
app.register_blueprint(documents_tags_bp)
app.register_blueprint(posts_tags_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(tag_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
