from models.post_model import Post, db
# post repository
class PostRepository:
    @staticmethod
    def get_all():
        return Post.query.all()
# get post by id
    @staticmethod
    def get_by_id(post_id):
        return Post.query.get(post_id)
# create post
    @staticmethod
    def create(post):
        db.session.add(post)
        db.session.commit()
        return post
# update post
    @staticmethod
    def update():
        db.session.commit()
# delete post
    @staticmethod
    def delete(post):
        db.session.delete(post)
        db.session.commit()
