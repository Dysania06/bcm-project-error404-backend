from flask import Flask
from flask_restful import Api
from flask_mysqldb import MySQL
from config import Config
from controller.user_controller import UsersResource, UserResource
from controller.document_controller import DocumentsResource, DocumentResource
from controller.post_controller import PostsResource, PostResource
from controller.tag_controller import TagsResource, TagResource
from controller.rating_controller import RatingsResource, RatingResource

app = Flask(__name__)
api = Api(app)

# Cấu hình MySQL
app.config['MYSQL_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_USER'] = Config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Config.MYSQL_DB
mysql = MySQL(app)

# Thêm routes
api.add_resource(UsersResource, '/api/users')
api.add_resource(UserResource, '/api/users/<string:user_id>')
api.add_resource(DocumentsResource, '/api/documents')
api.add_resource(DocumentResource, '/api/documents/<string:document_id>')
api.add_resource(PostsResource, '/api/posts')
api.add_resource(PostResource, '/api/posts/<string:post_id>')
api.add_resource(TagsResource, '/api/tags')
api.add_resource(TagResource, '/api/tags/<string:tag_id>')
api.add_resource(RatingsResource, '/api/ratings')
api.add_resource(RatingResource, '/api/ratings/<string:rating_id>')

if __name__ == '__main__':
    app.run(debug=False)
from flask_talisman import Talisman
Talisman(app, content_security_policy=None)  # Chống tấn công MITM