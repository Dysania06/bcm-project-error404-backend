from models.tag_model import Tag, db
# tag repository
class TagRepository:
    @staticmethod
    def get_all():
        return Tag.query.all()
# get tag by id
    @staticmethod
    def get_by_id(tag_id):
        return Tag.query.get(tag_id)
# create tag
    @staticmethod
    def create(tag):
        db.session.add(tag)
        db.session.commit()
        return tag
# update tag
    @staticmethod
    def update():
        db.session.commit()
# delete tag
    @staticmethod
    def delete(tag):
        db.session.delete(tag)
        db.session.commit()
