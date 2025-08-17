from models import Post, db

class PostController:
    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def create(data):
        new_post = Post(**data)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update(post, data):
        for key, value in data.items():
            setattr(post, key, value)
        db.session.commit()
        return post

    @staticmethod
    def delete(post):
        db.session.delete(post)
        db.session.commit()
