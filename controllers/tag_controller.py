from models import Tag, db

class TagController:
    @staticmethod
    def get_all():
        return Tag.query.all()

    @staticmethod
    def get_by_id(tag_id):
        return Tag.query.get(tag_id)

    @staticmethod
    def create(data):
        new_tag = Tag(**data)
        db.session.add(new_tag)
        db.session.commit()
        return new_tag

    @staticmethod
    def update(tag, data):
        for key, value in data.items():
            setattr(tag, key, value)
        db.session.commit()
        return tag

    @staticmethod
    def delete(tag):
        db.session.delete(tag)
        db.session.commit()
